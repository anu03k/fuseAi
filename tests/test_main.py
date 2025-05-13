from fastapi.testclient import TestClient
from app.main import app  # Adjust the import if your main file is elsewhere

client = TestClient(app)


def test_all_or_nothing():
    response = client.post("/check-distortion?thought=I always fail at everything")
    assert response.status_code == 200
    assert "all-or-nothing" in response.json()["distortion"]


def test_overgeneralization():
    response = client.post("/check-distortion?thought=Nothing ever goes right for me")
    assert response.status_code == 200
    assert "overgeneralization" in response.json()["distortion"]


def test_mental_filter():
    response = client.post("/check-distortion?thought=I only see my flaws")
    assert response.status_code == 200
    assert "mental filter" in response.json()["distortion"]


def test_personalization():
    response = client.post("/check-distortion?thought=It's all my fault we lost")
    assert response.status_code == 200
    assert "personalization" in response.json()["distortion"]


def test_no_distortion():
    response = client.post(
        "/check-distortion?thought=Today had both good and bad moments"
    )
    assert response.status_code == 200
    assert response.json()["distortion"] == []
