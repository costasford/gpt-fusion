import pytest

"""Backend tests that require FastAPI and httpx optional deps."""

pytest.importorskip("fastapi")
pytest.importorskip("httpx")

from fastapi.testclient import TestClient  # noqa: E402
from gpt_fusion.backend import app  # noqa: E402

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


def test_greet_user():
    response = client.get("/greet/Fusion")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Fusion! Welcome to gpt-fusion."}
