import time
from scraper.listing_parser import parse_listing_page
from scraper.detail_parser import parse_detail_page
from models import Project
from scraper.http_client import fetch_page_demo

def scrape_projects_demo(max_pages: int = 2):
    """
    Demonstrates scraping logic using local HTML files with simulated pagination.
    Supports multiple listing pages and corresponding detail pages.
    """
    all_projects = []

    for page in range(1, max_pages + 1):
        listing_file = f"listing_page_{page}.html"
        listing_soup = fetch_page_demo(listing_file)
        if not listing_soup:
            print(f"[Demo] Listing page {page} not found or invalid.")
            continue

        listing_projects = parse_listing_page(listing_soup)
        if not listing_projects:
            print(f"[Demo] No projects found on listing page {page}.")
            continue

        for basic_info in listing_projects:
            # Extract numeric part of project_id to match filenames
            project_id_full = basic_info['url'].rstrip("/").split("/")[-1]  # e.g., project-001
            project_number = project_id_full.split("-")[-1]  # "001", "002", etc.
            detail_file = f"project_detail_{project_number}.html"

            detail_soup = fetch_page_demo(detail_file)
            if not detail_soup:
                print(f"[Demo] Detail page for {basic_info['title']} not found.")
                continue

            project = parse_detail_page(detail_soup, basic_info)
            all_projects.append(project)

            time.sleep(0.2)  

    return all_projects
