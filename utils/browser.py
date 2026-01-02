# utils/browser.py
from playwright.sync_api import sync_playwright, Page, Browser, Playwright

def launch_browser(headless: bool = True, slow_mo: int = 0) -> tuple[Browser, Page, Playwright]:
    """
    Launches a Chromium browser instance using Playwright and returns the browser, page, and playwright objects.

    Args:
        headless (bool, optional): Whether to run the browser in headless mode. Defaults to True.
        slow_mo (int, optional): Delay in milliseconds between each action for debugging/observation. Defaults to 0.

    Returns:
        tuple[Browser, Page, Playwright]: Tuple containing the browser instance, a new page, and the Playwright object.
    """
    # Start Playwright
    playwright = sync_playwright().start()

    # Launch Chromium browser
    browser = playwright.chromium.launch(headless=headless, slow_mo=slow_mo)

    # Create a new browser context and page
    context = browser.new_context()
    page = context.new_page()

    return browser, page, playwright
