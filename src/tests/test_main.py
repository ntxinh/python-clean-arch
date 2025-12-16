from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_main():
    # Verify the API is up and running
    # Note: Swagger UI is at /docs, but let's check a 404 or a known endpoint
    response = client.get("/api/v1/todos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)