from fastapi.testclient import TestClient
from gpt_fusion.backend import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "gpt-fusion backend"}


def test_get_profile():
    response = client.get("/profile/test")
    assert response.status_code == 200
    assert response.json() == {"uid": "test", "display_name": "User test"}


def test_list_projects():
    response = client.get("/projects")
    assert response.status_code == 200
    data = response.json()
    assert any(p["id"] == "auth-ui-kit" for p in data)
