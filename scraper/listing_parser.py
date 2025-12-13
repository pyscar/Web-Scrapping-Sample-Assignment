from urllib.parse import urljoin
from utils import safe_text

BASE_URL = "https://www.adb.org"


def parse_listing_page(soup):
    """
    Parse the ADB projects listing page and extract
    basic project information available on the list view.

    Returns:
        List[dict]: Each dict contains title, url, country, sector
    """
    projects = []

    # Each project is inside a views-row
    rows = soup.select("div.view-content div.views-row")

    for row in rows:
        title_link = row.select_one("h3 a")
        if not title_link:
            # Defensive: skip malformed entries
            continue

        # Construct absolute URL
        project_url = urljoin(BASE_URL, title_link.get("href"))

        project_data = {
            "title": safe_text(title_link),
            "url": project_url,
            "country": safe_text(row.select_one(".field--name-field-country")),
            "sector": safe_text(row.select_one(".field--name-field-sector")),
        }

        projects.append(project_data)

    # log how many projects were found for debugging
    print(f"[Listing Parser] Found {len(projects)} projects on this page.")

    return projects
