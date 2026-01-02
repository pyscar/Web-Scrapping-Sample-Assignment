from playwright.sync_api import Page

def go_to_next_page(page: Page, next_selector: str = "a[rel='next']") -> bool:
    """
    Navigate to the next page if the next button exists and is enabled.

    Args:
        page (Page): Playwright Page object representing the current page.
        next_selector (str, optional): CSS selector for the "Next" button. Defaults to "a[rel='next']".

    Returns:
        bool: True if navigation to the next page occurred, False otherwise.
    """
    next_button = page.locator(next_selector)
    
    if next_button.count() > 0 and next_button.is_enabled():
        next_button.click()
        page.wait_for_load_state("networkidle")  # Wait until network requests are done
        return True
    
    return False
