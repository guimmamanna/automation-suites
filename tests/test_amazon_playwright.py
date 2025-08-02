import os
import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.fixture(scope="session")
def browser():
    """Launch a single browser instance for the test session."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    """Provide a new browser context and page for each test."""
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


def test_login_amazon(page):
    """Test logging into Amazon using credentials from environment variables."""
    email = os.environ.get("AMAZON_EMAIL")
    password = os.environ.get("AMAZON_PASSWORD")
    if not email or not password:
        pytest.skip("Missing AMAZON_EMAIL or AMAZON_PASSWORD environment variables")
    page.goto("https://www.amazon.co.uk")
    # Click sign-in link in the nav bar
    page.click("#nav-link-accountList")
    page.fill("input[name='email']", email)
    page.click("input#continue")
    page.fill("input[name='password']", password)
    page.click("input#signInSubmit")
    # Verify login by checking greeting text
    expect(page.locator('#nav-link-accountList-nav-line-1')).to_contain_text("Hello")


def test_search_product(page):
    """Test searching for a product on Amazon."""
    query = "playwright book"
    page.goto("https://www.amazon.co.uk")
    page.fill("input[name='field-keywords']", query)
    page.click("input#nav-search-submit-button")
    # Verify search results show the query
    expect(page.locator("span.a-color-state")).to_contain_text(query)


def test_add_to_cart(page):
    """Test adding an item to the shopping cart."""
    page.goto("https://www.amazon.co.uk")
    page.fill("input[name='field-keywords']", "usb cable")
    page.click("input#nav-search-submit-button")
    # Click the first search result's title link
    page.locator("div[data-component-type='s-search-result'] h2 a").first.click()
    # Wait and click add to cart
    page.wait_for_selector("#add-to-cart-button", timeout=10000)
    page.click("#add-to-cart-button")
    # Verify cart count has incremented
    page.wait_for_selector("#nav-cart-count", timeout=10000)
    cart_count = int(page.inner_text("#nav-cart-count"))
    assert cart_count >= 1
