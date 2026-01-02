from playwright.sync_api import Page
from models.project_model import Project
from utils.pagination import go_to_next_page  # Reusable pagination helper

def scrape_projects(page: Page, start_url: str, max_pages: int = 1) -> list[Project]:
    """
    Scrapes projects from the ADB projects page.

    Args:
        page (Page): Playwright page instance.
        start_url (str): URL of the projects listing page.
        max_pages (int, optional): Maximum number of pages to scrape. Defaults to 1.

    Returns:
        list[Project]: List of Project objects with extracted data.
    """
    projects = []

    # --- Navigate to the starting page ---
    page.goto(start_url, wait_until="domcontentloaded")
    page.wait_for_timeout(3000)  # Wait for content to load

    # --- Cloudflare / protection detection ---
    html = page.content().lower()
    if "cloudflare" in html or "attention required" in html or "blocked" in html:
        print("❌ Access blocked by Cloudflare / protection detected.")
        print("🛑 Stopping scraper to avoid retries.")
        return projects
    else:
        print("✅ Page content looks normal. Proceeding with scrape.")

    current_page = 1

    # --- Main scraping loop ---
    while current_page <= max_pages:
        # Locate all project cards on the current page
        cards = page.locator("div.item.linked")
        card_count = cards.count()
        print(f"Page {current_page} - Cards found:", card_count)

        if card_count == 0:
            print("⚠️ No cards found. Possible DOM change or soft block.")
            break

        # --- Extract data for each project ---
        for i in range(card_count):
            card = cards.nth(i)

            # --- Title & URL ---
            title_el = card.locator("div.item-title a")
            title = title_el.inner_text().strip()
            relative_url = title_el.get_attribute("href")
            project_url = f"https://www.adb.org{relative_url}" if relative_url else ""

            # --- Project summary: ID, country, sector ---
            project_id, country, sector = "", "", ""
            summary_el = card.locator("div.item-summary")
            if summary_el.count() > 0:
                raw_summary = summary_el.inner_text().strip()
                delimiter = ";" if ";" in raw_summary else ","
                parts = [p.strip() for p in raw_summary.split(delimiter)]
                if len(parts) > 0:
                    project_id = parts[0]
                if len(parts) > 1:
                    country = parts[1]
                if len(parts) > 2:
                    sector = parts[2]

            # --- Status ---
            status_el = card.locator(
                "div.item-meta span.Approved, div.item-meta span.Closed, div.item-meta span.Active"
            )
            status = status_el.inner_text().strip() if status_el.count() > 0 else ""

            # --- Approval year ---
            approval_year = ""
            approval_date_el = card.locator("div.item-meta time")
            if approval_date_el.count() > 0:
                datetime_value = approval_date_el.get_attribute("datetime")
                approval_year = datetime_value[:4] if datetime_value else ""

            # --- Append Project object ---
            projects.append(
                Project(
                    title=title,
                    country=country,
                    sector=sector,
                    status=status,
                    approval_year=approval_year,
                    project_id=project_id,
                    project_url=project_url
                )
            )

        # --- Pagination: move to the next page if available ---
        if not go_to_next_page(page):
            break
        current_page += 1

    return projects
