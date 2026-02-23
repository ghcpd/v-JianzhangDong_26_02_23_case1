from pathlib import Path

from fastapi import FastAPI

from .config import load_yaml_config
from .models import ReportRequest, SummaryResponse
from .services import generate_summary

# Resolve config relative to this file for local runs and tests
CONFIG_PATH = Path(__file__).parent / "config.yaml"
config = load_yaml_config(CONFIG_PATH)

app = FastAPI(title=config.app_name, debug=config.debug)


@app.get("/health")
def health():
    return {"status": "ok", "app": config.app_name}


@app.post("/report/summary", response_model=SummaryResponse)
def summary(request: ReportRequest):
    # In a real implementation, you might filter data based on request.start_date/end_date
    return generate_summary()
