from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_click():
    response = client.post("/click")
    assert response.status_code == 200
    assert "clicks" in response.json()

def test_status():
    response = client.get("/status")
    assert response.status_code == 200
    assert "clicks" in response.json()