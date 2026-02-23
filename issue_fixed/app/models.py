from datetime import datetime
from pydantic import BaseModel, Field


class ReportRequest(BaseModel):
    start_date: datetime = Field(..., description="Start of report range")
    end_date: datetime = Field(..., description="End of report range")
