# automation-suites

This repository contains a collection of automation test suites for QA projects. It includes examples written in Python using frameworks such as **pytest**, **Selenium**, and **Playwright**.

## Getting started

1. Clone this repository:

        git clone https://github.com/guimmamanna/automation-suites.git
        cd automation-suites

2. Create a virtual environment and install dependencies:

        python -m venv venv
        source venv/bin/activate  # On Windows use venv\Scripts\activate
        pip install -r requirements.txt

3. (Optional) Install Playwright browsers:

        playwright install

## Running tests

This project uses **pytest**. To run all tests:

        pytest

To run a specific test file:

        pytest tests/test_amazon_playwright.py

## Amazon Playwright suite

The `tests/test_amazon_playwright.py` script provides a Playwright-based automation suite for testing an e-commerce site. It demonstrates how to:

- Log in to Amazon with credentials from environment variables.
- Search for a product.
- Add an item to the cart.

Before running these tests you must set the following environment variables with your Amazon credentials:

        export AMAZON_EMAIL="your-email@example.com"
        export AMAZON_PASSWORD="your-password"

If the variables are not set the login test will be skipped. The search and add-to-cart tests do not require an authenticated session but may behave differently when not logged in.

**Note:** These tests are provided for educational purposes. Do not commit your real credentials to version control.

## Contributing

Feel free to open issues or submit pull requests with improvements or additional test suites. Contributions are welcome.
