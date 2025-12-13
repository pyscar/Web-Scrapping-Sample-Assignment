from dataclasses import dataclass
from typing import Optional


@dataclass
class Project:
    project_id: str
    title: str
    url: str

    country: Optional[str] = None
    sector: Optional[str] = None
    status: Optional[str] = None
    approval_date: Optional[str] = None
    amount: Optional[str] = None
    executing_agency: Optional[str] = None
    description: Optional[str] = None
