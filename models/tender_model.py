from dataclasses import dataclass

@dataclass
class Tender:
    title: str
    tender_url: str
    project_id: str
    region: str
    sector: str
    posting_date: str
    status: str
    notice_type: str
