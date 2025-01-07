# app.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
print("123")
@app.get("/get_version")
def get_version():
    return {"version": "1.0.0"}

@app.get("/check_prime/{number}")
def check_prime(number: int):
    if number < 2:
        return {"number": number, "is_prime": False}
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return {"number": number, "is_prime": False}
    return {"number": number, "is_prime": True}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
