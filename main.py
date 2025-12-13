import json
import csv
from scraper.scraper import scrape_projects_demo

def main():
    print("Starting ADB project scraping demo...")

    projects = scrape_projects_demo()
    if not projects:
        print("No projects were scraped. Exiting.")
        return

    # Convert dataclass objects to dictionaries
    projects_data = [project.__dict__ for project in projects]

    # Save JSON
    json_file = "adb_projects_demo.json"
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(projects_data, f, ensure_ascii=False, indent=4)
    print(f"Demo scraping completed. {len(projects)} projects saved to {json_file}")

    # Save CSV
    csv_file = "adb_projects_demo.csv"
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=projects_data[0].keys())
        writer.writeheader()
        writer.writerows(projects_data)
    print(f"CSV file also saved as {csv_file}")


if __name__ == "__main__":
    main()
