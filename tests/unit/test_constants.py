from house_prices import constants


def test_zillow_clone_url_uses_https() -> None:
    assert constants.ZILLOW_CLONE_URL.startswith("https")


def test_request_headers_contain_user_agent_and_language() -> None:
    assert "User-Agent" in constants.REQUEST_HEADERS
    assert "Accept-Language" in constants.REQUEST_HEADERS
