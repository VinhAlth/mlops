from fastapi import FastAPI
from pydantic import BaseModel
import math

app = FastAPI()

# Route để lấy phiên bản của ứng dụng
@app.get("/get_version")
def get_version():
    return {"version": "1.0.0"}

# Hàm kiểm tra số nguyên tố
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Route để kiểm tra số nguyên tố
@app.get("/check_prime/{number}")
def check_prime(number: int):
    return {"number": number, "is_prime": is_prime(number)}

