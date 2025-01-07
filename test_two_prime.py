import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

# Test route get_version
def test_get_version_updated():
    response = client.get("/get_version")
    assert response.status_code == 200
    # Giả định phiên bản mới là "1.0.1"
    assert response.json() == {"version": "1.0.1"}

# Test route check_prime with new test cases
@pytest.mark.parametrize("number, expected", [
    (-1, False),  # Số âm không phải số nguyên tố
    (0, False),   # Số 0 không phải số nguyên tố
    (1, False),   # Số 1 không phải số nguyên tố
    (19, True),   # Số nguyên tố lẻ lớn hơn
    (23, True),   # Số nguyên tố lẻ lớn hơn
    (25, False),  # Số lẻ không phải số nguyên tố (bị chia hết bởi 5)
    (29, True),   # Số nguyên tố lớn
    (31, True),   # Số nguyên tố lớn
    (100, False), # Số chẵn lớn
    (101, True),  # Số nguyên tố lẻ lớn
])
def test_check_prime_new_cases(number, expected):
    response = client.get(f"/check_prime/{number}")
    assert response.status_code == 200
    assert response.json()["is_prime"] == expected
