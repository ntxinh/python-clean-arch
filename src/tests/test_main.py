import pytest
from fastapi.testclient import TestClient
from src.main import app


# 1. Create a fixture that handles the startup/shutdown logic
@pytest.fixture
def client():
    # 'with TestClient' triggers the lifespan event (running init_db)
    with TestClient(app) as c:
        yield c


# 2. Inject the 'client' fixture into test
def test_read_main(client):
    response = client.get("/api/v1/todos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
