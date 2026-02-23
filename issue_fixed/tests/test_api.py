from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_summary():
    payload = {
        "start_date": "2024-01-01T00:00:00",
        "end_date": "2024-02-01T00:00:00",
    }
    r = client.post("/report/summary", json=payload)
    assert r.status_code == 200
    body = r.json()
    assert "mean" in body
    assert body["max"] <= 100
