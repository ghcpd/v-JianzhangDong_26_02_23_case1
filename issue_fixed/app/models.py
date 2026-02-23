from pydantic import BaseModel
from datetime import datetime

class ReportRequest(BaseModel):
    start_date: datetime
    end_date: datetime
