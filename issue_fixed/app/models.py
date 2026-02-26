from datetime import datetime
from typing import Optional

from packaging.version import Version
from pydantic import BaseModel, Field, __version__ as pydantic_version

IS_PYDANTIC_V2 = Version(pydantic_version) >= Version("2.0")


class ReportRequest(BaseModel):
    start_date: datetime = Field(..., description="ISO8601 start date")
    end_date: datetime = Field(..., description="ISO8601 end date")
    # Additional filters can be added later (e.g., user_id, tags)

    if IS_PYDANTIC_V2:
        model_config = {
            "json_schema_extra": {
                "examples": [
                    {
                        "start_date": "2024-01-01T00:00:00",
                        "end_date": "2024-02-01T00:00:00",
                    }
                ]
            }
        }
    else:
        class Config:  # type: ignore[override]
            schema_extra = {
                "example": {
                    "start_date": "2024-01-01T00:00:00",
                    "end_date": "2024-02-01T00:00:00",
                }
            }


class SummaryResponse(BaseModel):
    mean: float
    max: int
    generated_at: datetime
    rows: int
    sample: Optional[list[int]] = None

    if IS_PYDANTIC_V2:
        model_config = {
            "json_schema_extra": {
                "examples": [
                    {
                        "mean": 50.5,
                        "max": 99,
                        "generated_at": "2024-01-01T00:00:00",
                        "rows": 100,
                    }
                ]
            }
        }
    else:
        class Config:  # type: ignore[override]
            schema_extra = {
                "example": {
                    "mean": 50.5,
                    "max": 99,
                    "generated_at": "2024-01-01T00:00:00",
                    "rows": 100,
                }
            }

