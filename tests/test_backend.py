from fastapi.testclient import TestClient
from gpt_fusion.backend import app

client = TestClient(app)


def test_get_profile():
    response = client.get("/profile/test")
    assert response.status_code == 200
    assert response.json() == {"uid": "test", "display_name": "User test"}
