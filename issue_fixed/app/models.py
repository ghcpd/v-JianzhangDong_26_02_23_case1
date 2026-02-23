from pydantic import BaseModel
from datetime import datetime

class ReportRequest(BaseModel):
    start_date: str
    end_date: str