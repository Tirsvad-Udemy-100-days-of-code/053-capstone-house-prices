"""End-to-end test: fills a fake form with headless Chrome. Runs only in Docker."""

import json
import os
import threading
from collections.abc import Iterator
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

import pytest

from house_prices.application.use_cases.fill_form import FillForm
from house_prices.infrastructure.beautifulsoup_listing_parser import (
    BeautifulSoupListingParser,
)
from house_prices.infrastructure.chrome_driver_factory import create_chrome_driver
from house_prices.infrastructure.selenium_form_submitter import (
    SeleniumFormSubmitter,
)

FIXTURE = Path(__file__).parent.parent / "fixtures" / "zillow_clone.html"
RESULTS_DIR_ENV_VAR = "RESULTS_DIR"
LISTING_COUNT = 3

PAGE = """<!doctype html>
<html><body>
<input type="text" id="a"><input type="text" id="b"><input type="text" id="c">
<div role="button" id="go"><span>Submit</span></div>
<p id="done"></p>
<script>
document.getElementById("go").addEventListener("click", async () => {
  const values = ["a", "b", "c"].map((id) => document.getElementById(id).value);
  await fetch("/submit", {method: "POST", body: JSON.stringify(values)});
  document.getElementById("done").textContent = "Your response has been recorded";
});
</script>
</body></html>
"""


class FormServer(HTTPServer):
    submissions: list[list[str]]


class Handler(BaseHTTPRequestHandler):
    server: FormServer

    def do_GET(self) -> None:  # noqa: N802
        body = PAGE.encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self) -> None:  # noqa: N802
        length = int(self.headers["Content-Length"])
        self.server.submissions.append(json.loads(self.rfile.read(length)))
        self.send_response(204)
        self.end_headers()

    def log_message(self, format: str, *args: object) -> None:  # noqa: A002
        return


@pytest.fixture
def server() -> Iterator[FormServer]:
    httpd = FormServer(("127.0.0.1", 0), Handler)
    httpd.submissions = []
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    yield httpd
    httpd.shutdown()
    httpd.server_close()


@pytest.mark.e2e
def test_submitter_records_one_response_per_listing(server: FormServer) -> None:
    html = FIXTURE.read_text(encoding="utf-8")
    listings = BeautifulSoupListingParser().parse(html)[:LISTING_COUNT]
    url = f"http://127.0.0.1:{server.server_port}/"
    driver = create_chrome_driver(headless=True)
    try:
        count = FillForm(SeleniumFormSubmitter(driver, url)).execute(listings)
        results_dir = os.environ.get(RESULTS_DIR_ENV_VAR)
        if results_dir:
            Path(results_dir).mkdir(parents=True, exist_ok=True)
            driver.save_screenshot(str(Path(results_dir) / "e2e-form-filled.png"))
    finally:
        driver.quit()

    assert count == LISTING_COUNT
    assert server.submissions == [[x.address, x.price, x.link] for x in listings]
