from dataclasses import dataclass

@dataclass
class Project:
    title: str
    country: str
    sector: str
    status: str
    approval_year: str
    project_id: str
    project_url: str
