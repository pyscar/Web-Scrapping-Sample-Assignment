from bs4 import BeautifulSoup

def fetch_page_demo(file_path: str) -> BeautifulSoup | None:
    """
    Loads a local HTML file and returns a BeautifulSoup object.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return BeautifulSoup(f.read(), "html.parser")
    except FileNotFoundError:
        print(f"[Demo Fetch] File not found: {file_path}")
        return None
