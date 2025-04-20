from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}

def test_rank_endpoint():
    payload = {
        "resume": "Python developer",
          "job_description": "Looking for backend dev"
    }
    res = client.post("/rank", json=payload)
    assert res.status_code == 200
    assert "score" in res.json()


def test_rank_and_db():
    payload = {
        "resume": "Python fastapi & Django backend developer",
          "job_description": "Looking for Python backend experience"
    }
    res = client.post("/rank", json=payload)
    assert res.status_code == 200
    assert "score" in res.json()
