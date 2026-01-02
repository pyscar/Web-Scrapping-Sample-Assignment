# ADB Web Scraper 🏦

[![Python](https://img.shields.io/badge/python-3.13-blue)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/playwright-1.40-orange)](https://playwright.dev/)
[![License](https://img.shields.io/badge/license-educational-lightgrey)](LICENSE)

A modular Python web scraper to extract **Projects, Documents, and Tenders** from the [Asian Development Bank (ADB)](https://www.adb.org/) website. Built with **Playwright**, it supports multi-page scraping, Cloudflare detection, and CSV export.

---

## 🗂 Project Structure

```
adb_scraper/
│
├── scraper/ 
│   ├── projects.py       # Scraper for Projects
│   ├── documents.py      # Scraper for Documents
│   ├── tenders.py        # Scraper for Tenders
│
├── models/
│   ├── project_model.py
│   ├── document_model.py
│   ├── tender_model.py
│
├── utils/
│   ├── browser.py        # Browser launch helper
│   ├── pagination.py     # Pagination helper
│   ├── csv_writer.py     # CSV saving functions
│
└── main.py               # Entry point to run all scrapers
```

---

## ✨ Features

* **Modular Scrapers**: Separate scrapers for Projects, Documents, and Tenders.
* **Multi-page Support**: Handles pagination via helper functions.
* **Protection Detection**: Stops automatically if Cloudflare or other protection pages appear.
* **CSV Export**: Saves scraped data in clean CSV files.
* **Configurable Browser**: Supports headless mode and slow-motion navigation for debugging.

---

## ⚡ Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd adb_scraper
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

3. Install dependencies and browsers:

```bash
pip install playwright
playwright install
```

---

## 🚀 Usage

Run the main scraper:

```bash
python main.py
```

The script will:

1. Launch a browser.
2. Scrape **Projects** → save `projects.csv`.
3. Scrape **Documents** → save `documents.csv`.
4. Scrape **Tenders** → save `tenders.csv`.
5. Close the browser automatically.

---

## ⚙️ Configuration

* **Headless Mode**: Set `headless=True/False` in `launch_browser()`.
* **Slow Motion**: Adjust `slow_mo` in `launch_browser()` to slow down interactions.
* **Page Limit**: Control the number of pages scraped via `max_pages` in each scraper.

---

## 📄 Example CSV Output

**Projects**: `title, country, sector, status, approval_year, project_id, project_url`
**Documents**: `title, project_id, region, document_type, upload_date, document_url`
**Tenders**: `title, tender_url, project_id, region, sector, posting_date, status, notice_type`

---

## ⚠️ Notes

* This project demonstrates **scraping logic, structure, and handling of pagination/protection**.
* Running the scraper on ADB may trigger **Cloudflare protection**, which stops scraping automatically.
* CSV files are saved in the project root directory.

---

## 📜 License

Educational use only. Use responsibly and comply with website terms of service.



Do you want me to make that version too?
