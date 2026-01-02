from time import sleep
from Scraper.projects import scrape_projects
from Scraper.documents import scrape_documents
from Scraper.tenders import scrape_tenders
from utils.csv_writer import save_projects_to_csv, save_documents_to_csv, save_tenders_to_csv
from utils.browser import launch_browser  

# --- URLs for scraping ---
PROJECTS_URL = "https://www.adb.org/projects"
DOCUMENTS_URL = "https://www.adb.org/projects/documents"
TENDERS_URL = "https://www.adb.org/projects/tenders"

# --- Launch browser ---
browser, page, playwright = launch_browser(headless=False, slow_mo=800)

try:
    # -------------------------
    # Scrape Projects
    # -------------------------
    print("Scraping Projects...")
    projects = scrape_projects(page, PROJECTS_URL, max_pages=1)  # max_pages can be adjusted
    save_projects_to_csv(projects, "projects.csv")
    print(f"✅ Projects saved: {len(projects)}")

    # -------------------------
    # Wait before next scrape
    # -------------------------
    print("⏱ Waiting 5 seconds before scraping Documents...")
    sleep(5)

    # -------------------------
    # Scrape Documents
    # -------------------------
    print("Scraping Documents...")
    documents = scrape_documents(page, DOCUMENTS_URL, max_pages=1)
    save_documents_to_csv(documents, "documents.csv")
    print(f"✅ Documents saved: {len(documents)}")

    # -------------------------
    # Wait before next scrape
    # -------------------------
    print("⏱ Waiting 5 seconds before scraping Tenders...")
    sleep(5)

    # -------------------------
    # Scrape Tenders
    # -------------------------
    print("Scraping Tenders...")
    tenders = scrape_tenders(page, TENDERS_URL, max_pages=1)
    save_tenders_to_csv(tenders, "tenders.csv")
    print(f"✅ Tenders saved: {len(tenders)}")

finally:
    # -------------------------
    # Close browser and stop playwright
    # -------------------------
    browser.close()
    playwright.stop()

