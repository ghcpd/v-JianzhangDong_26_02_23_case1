from pydantic import BaseModel
import pandas as pd
import numpy as np


class ReportRequest(BaseModel):
    start_date: str
    end_date: str


def generate_summary():
    df = pd.DataFrame({
        "value": np.random.randint(1, 100, 100)
    })
    return {
        "mean": float(df["value"].mean()),
        "max": int(df["value"].max()),
    }
