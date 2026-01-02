import csv
from typing import List
from models.project_model import Project
from models.document_model import Document
from models.tender_model import Tender

def save_projects_to_csv(projects: List[Project], file_path: str):
    """
    Save a list of Project objects to a CSV file.

    Args:
        projects (List[Project]): List of Project instances.
        file_path (str): Path to the output CSV file.
    """
    with open(file_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        # Write CSV headers based on Project dataclass fields
        writer.writerow(Project.__annotations__.keys())
        # Write project data
        for project in projects:
            writer.writerow(project.__dict__.values())

def save_documents_to_csv(documents: List[Document], file_path: str):
    """
    Save a list of Document objects to a CSV file.

    Args:
        documents (List[Document]): List of Document instances.
        file_path (str): Path to the output CSV file.
    """
    with open(file_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(Document.__annotations__.keys())
        for doc in documents:
            writer.writerow(doc.__dict__.values())

def save_tenders_to_csv(tenders: List[Tender], file_path: str):
    """
    Save a list of Tender objects to a CSV file.

    Args:
        tenders (List[Tender]): List of Tender instances.
        file_path (str): Path to the output CSV file.
    """
    with open(file_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(Tender.__annotations__.keys())
        for tender in tenders:
            writer.writerow(tender.__dict__.values())
