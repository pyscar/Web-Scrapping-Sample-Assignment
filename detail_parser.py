from models import Project
from utils import safe_text
from bs4 import BeautifulSoup


def parse_detail_page(soup: BeautifulSoup, basic_info: dict) -> Project:
    """
    Parse an individual ADB project detail page and return a Project object.
    
    Args:
        soup (BeautifulSoup): Parsed project detail page.
        basic_info (dict): Contains 'title' and 'url' from listing page.

    Returns:
        Project: Complete project information.
    """

    def extract_labeled_field(label: str) -> str | None:
        """
        Extract value corresponding to a label from ADB field layout:
            <div class="field--label">Label</div>
            <div class="field--item">Value</div>
        """
        label_div = soup.find("div", class_="field--label", string=label)
        if not label_div:
            return None
        value_div = label_div.find_next_sibling("div", class_="field--item")
        return safe_text(value_div)

    project_id = basic_info.get("url", "").rstrip("/").split("/")[-1]

    return Project(
        project_id=project_id,
        title=basic_info.get("title"),
        url=basic_info.get("url"),
        country=extract_labeled_field("Country"),
        sector=extract_labeled_field("Sector"),
        status=extract_labeled_field("Status"),
        approval_date=extract_labeled_field("Approval Date"),
        amount=extract_labeled_field("Amount"),
        executing_agency=extract_labeled_field("Executing Agency"),
        description=safe_text(soup.select_one("div.field--name-field-description"))
    )
