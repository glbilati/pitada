from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_healthz() -> None:
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_errors_follow_rfc7807() -> None:
    response = client.get("/api/v1/me")
    assert response.status_code == 501
    assert response.headers["content-type"].startswith("application/problem+json")
    body = response.json()
    assert body["status"] == 501
    assert "title" in body


def test_validation_error_is_problem_json() -> None:
    response = client.post("/api/v1/auth/login", json={"email": "a@b.c"})
    assert response.status_code == 422
    assert response.headers["content-type"].startswith("application/problem+json")


def test_unknown_route_is_problem_json() -> None:
    response = client.get("/api/v1/nao-existe")
    assert response.status_code == 404
    assert response.headers["content-type"].startswith("application/problem+json")
