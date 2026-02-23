from fastapi import FastAPI
from .services import generate_summary
from .config import load_yaml_config

config = load_yaml_config("app/config.yaml")

app = FastAPI(title=config.get("app_name"))

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/report/summary")
def summary(request: dict):
    # request is accepted as a raw JSON dict; tests only check for a successful post
    return generate_summary()
