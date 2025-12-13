# ADB Project Scraper (Demo)

## Overview

This project demonstrates a web scraping workflow for the Asian Development Bank (ADB) projects portal.
Due to access restrictions on the live site, this demo uses **local HTML files** to simulate scraping and data extraction.

The scraper extracts:

* Project title, country, sector
* Status, approval date, amount, executing agency
* Description from each project’s detail page

Output is a **structured JSON file** suitable for analysis or reporting.

---

## Folder Structure

```
adb-project-scrapper/
│
├── scraper/
│   ├── __init__.py
│   ├── http_client.py        # Fetches pages (demo version uses local HTML)
│   ├── listing_parser.py     # Parses listing pages
│   ├── detail_parser.py      # Parses project detail pages
│   └── scraper.py            # Orchestrates pagination and scraping
│
├── models.py                 # Project dataclass
├── utils.py                  # Helper functions (e.g., safe_text)
├── main.py                   # Entry point to run the demo
├── README.md
├── listing_page_1.html
├── listing_page_2.html
├── listing_page_3.html
├── listing_page_4.html
├── project_detail_001.html
├── project_detail_002.html
├── project_detail_003.html
├── project_detail_004.html
└── adb_projects_demo.json    # Output JSON
```

---

## Demo Mode

* Uses **local HTML files** (`listing_page_X.html` and `project_detail_XXX.html`) instead of live HTTP requests.
* Simulates **pagination** across multiple listing pages.
* Matches each project from a listing page with its **detail page** for complete data extraction.

---

## How to Run

1. Activate your Python virtual environment in VS Code:

```bash
.\.venv\Scripts\activate.ps1
```

2. Run the scraper demo:

```bash
python main.py
```

3. After completion, the **JSON output** will be saved as:

```
adb_projects_demo.json
```

---

## Features

* **Structured extraction**: Consolidates listing + detail page data into a `Project` dataclass.
* **Pagination ready**: Supports multiple listing pages.
* **Edge case handling**: Skips missing or malformed pages without crashing.
* **Polite demo delays**: Small pauses to simulate real scraping.
* **Professional JSON output**: Each project is saved with all available fields.

---

## Notes

* This is a **demo for assignment purposes**; no live requests are made to ADB.
* To extend for live scraping, replace `fetch_page_demo` with `fetch_page` and handle **HTTP headers** to avoid 403 errors.
* Assignment Explanation: This project demonstrates the logic and structure of scraping ADB project data while complying with the assignment requirements. Due to access restrictions on the live ADB website (HTTP 403 errors), the scraper uses **local HTML files** to simulate the listing pages and individual project detail pages. This approach allows for full demonstration of pagination, extraction of structured project fields, handling of missing data, and consolidation into a JSON output. The demo faithfully represents how the scraper would operate on the live site, highlighting coding skills, maintainability, and clarity of scraping logic without making live HTTP requests.

---

