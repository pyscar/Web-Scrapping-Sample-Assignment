from playwright.sync_api import Page
from models.tender_model import Tender
from utils.pagination import go_to_next_page  # reusable pagination
import re

def scrape_tenders(page: Page, start_url: str, max_pages: int = 1) -> list[Tender]:
    """
    Scrapes tender data from the ADB tenders page.

    Args:
        page (Page): Playwright page instance.
        start_url (str): URL of the tenders listing page.
        max_pages (int, optional): Maximum number of pages to scrape. Defaults to 1.

    Returns:
        list[Tender]: List of Tender objects with extracted data.
    """
    tenders = []

    # --- Navigate to the starting page ---
    page.goto(start_url, wait_until="domcontentloaded")
    page.wait_for_timeout(3000)

    # --- Cloudflare / protection detection ---
    html = page.content().lower()
    if "cloudflare" in html or "attention required" in html or "blocked" in html:
        print("❌ Access blocked by Cloudflare / protection detected.")
        print("🛑 Stopping scraper to avoid retries.")
        return tenders
    else:
        print("✅ Page content looks normal. Proceeding with scrape.")

    current_page = 1

    # --- Main scraping loop ---
    while current_page <= max_pages:
        # Locate all tender cards on the current page
        cards = page.locator("div.item.linked")
        card_count = cards.count()
        print(f"Page {current_page} - Tenders found:", card_count)

        if card_count == 0:
            print("⚠️ No tenders found. Possible DOM change or soft block.")
            break

        # --- Extract data for each tender ---
        for i in range(card_count):
            card = cards.nth(i)

            # --- Title & URL ---
            title_el = card.locator("div.item-title a")
            title = title_el.inner_text().strip()
            relative_url = title_el.get_attribute("href")
            tender_url = f"https://www.adb.org{relative_url}" if relative_url else ""

            # --- Summary: Project ID, Region, Sector, Posting Date ---
            project_id, region, sector, posting_date = "", "", "", ""
            summary_el = card.locator("div.item-summary")
            if summary_el.count() > 0:
                raw_summary = summary_el.inner_text().strip()
                parts = [p.strip() for p in raw_summary.split(";")]

                if len(parts) > 0:
                    project_id = parts[0]
                if len(parts) > 1:
                    region = parts[1]
                if len(parts) > 2:
                    sector = parts[2]
                if len(parts) > 3:
                    match = re.search(r"Posting date:\s*(.*)", parts[3], re.I)
                    if match:
                        posting_date = match.group(1).strip()

            # --- Status ---
            status_el = card.locator(
                "div.item-meta span.Active, div.item-meta span.Closed, div.item-meta span.Awarded"
            )
            status = status_el.inner_text().strip() if status_el.count() > 0 else ""

            # --- Notice Type ---
            notice_type = ""
            notice_el = card.locator("div.item-details span")
            if notice_el.count() >= 2:
                notice_type = notice_el.nth(1).inner_text().strip()

            # --- Append Tender object ---
            tenders.append(
                Tender(
                    title=title,
                    tender_url=tender_url,
                    project_id=project_id,
                    region=region,
                    sector=sector,
                    posting_date=posting_date,
                    status=status,
                    notice_type=notice_type
                )
            )

        # --- Pagination: move to the next page if available ---
        if not go_to_next_page(page):
            break
        current_page += 1

    return tenders
