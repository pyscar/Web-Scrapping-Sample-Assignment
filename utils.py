def safe_text(element):
    """
    Safely extract cleaned text from a BeautifulSoup element.
    Returns None if the element is missing.
    """
    if element is None:
        return None
    return element.get_text(strip=True)
