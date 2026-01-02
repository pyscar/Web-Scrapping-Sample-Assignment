from playwright.sync_api import Page
from models.document_model import Document
from utils.pagination import go_to_next_page

def scrape_documents(page: Page, start_url: str, max_pages: int = 1) -> list[Document]:
    """
    Scrapes documents from the ADB website.

    Args:
        page (Page): Playwright page instance.
        start_url (str): URL of the documents listing page.
        max_pages (int, optional): Maximum number of pages to scrape. Defaults to 1.

    Returns:
        list[Document]: List of Document objects containing extracted data.
    """
    documents = []

    # --- Navigate to the starting page ---
    page.goto(start_url, wait_until="domcontentloaded")
    page.wait_for_timeout(3000)  # Give time for the page to fully load

    # --- Cloudflare / protection detection ---
    html = page.content().lower()
    if "cloudflare" in html or "attention required" in html or "blocked" in html:
        print("❌ Access blocked by Cloudflare / protection detected.")
        print("🛑 Stopping scraper to avoid retries.")
        return documents
    else:
        print("✅ Page content looks normal. Proceeding with scrape.")

    current_page = 1

    # --- Main scraping loop across pages ---
    while current_page <= max_pages:
        # Locate all document cards on the current page
        cards = page.locator("div.item.linked")
        print(f"Page {current_page} - Documents found:", cards.count())

        # --- Extract data for each document ---
        for i in range(cards.count()):
            card = cards.nth(i)

            # --- Title & URL ---
            title_el = card.locator("div.item-title a")
            title = title_el.inner_text().strip()
            relative_url = title_el.get_attribute("href")
            document_url = f"https://www.adb.org{relative_url}" if relative_url else ""

            # --- Document meta: Upload date ---
            upload_date = ""
            date_el = card.locator("div.item-meta time")
            if date_el.count() > 0:
                upload_date = date_el.get_attribute("datetime") or ""

            # --- Document summary: Project ID, Region, Document Type ---
            project_id = ""
            region = ""
            document_type = ""
            summary_el = card.locator("div.views-field.views-field-nothing span.field-content")
            if summary_el.count() > 0:
                raw_summary = summary_el.inner_text().strip()
                parts = [p.strip() for p in raw_summary.split(";")]

                if len(parts) > 0:
                    project_id = parts[0]
                if len(parts) > 1:
                    region = parts[1]
                if len(parts) > 2:
                    # Remove "Type:" prefix if present
                    document_type = parts[2].replace("Type:", "").strip()

            # --- Create Document object and append to list ---
            documents.append(
                Document(
                    title=title,
                    project_id=project_id,
                    region=region,
                    document_type=document_type,
                    upload_date=upload_date,
                    document_url=document_url
                )
            )

        # --- Pagination: move to the next page if available ---
        if not go_to_next_page(page):
            break
        current_page += 1

    return documents
