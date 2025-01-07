import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)
print("Helooooo")
# Test route get_version
def test_get_version():
    response = client.get("/get_version")
    assert response.status_code == 200
    assert response.json() == {"version": "1.0.0"}

# Test route check_prime
@pytest.mark.parametrize("number, expected", [
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (9, False),
    (10, False),
    (11, True),
    (15, False),
    (17, True),
    (18, False),
])
def test_check_prime(number, expected):
    response = client.get(f"/check_prime/{number}")
    assert response.status_code == 200
    assert response.json()["is_prime"] == expected

