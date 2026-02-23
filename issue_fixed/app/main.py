from fastapi import FastAPI
from .models import ReportRequest
from .services import generate_summary
from .config import load_yaml_config

config = load_yaml_config("app/config.yaml")

app = FastAPI(title=config.app_name)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/report/summary")
def summary(request: ReportRequest):
    return generate_summary()
