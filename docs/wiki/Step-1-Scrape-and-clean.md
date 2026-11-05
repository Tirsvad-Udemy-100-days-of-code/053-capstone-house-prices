**English** · [Dansk](Step-1-Scrape-and-clean-da) · [Bahasa Malaysia](Step-1-Scrape-and-clean-ms)

# Step 1: Scrape and clean

We downloaded the page with `requests`, sending a `User-Agent` and an `Accept-Language` header so that the site answers like it does for a browser, and read it with BeautifulSoup. We cleaned the text: prices become `$1,234`, and addresses lose newlines, pipes and extra spaces. The screenshot shows the result of `python -m house_prices --scrape-only`.

![Step 1: Scrape and clean](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/053-capstone-house-prices/raw/branch/main/docs/images/01-scrape-output.png)

## What we gained

- Request headers decide what a website sends back.
- CSS selectors find the links, addresses and prices in the HTML.
- Cleaning is a small pure function (`clean_price`, `clean_address`), so it is easy to test with a saved copy of the page.
- The lists keep the names of the assignment: `get_links`, `get_addresses`, `get_prices`.

Back to [Home](Home)
