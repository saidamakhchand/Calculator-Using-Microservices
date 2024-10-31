# calculator_api.py
from fastapi import FastAPI
import httpx
from pydantic import BaseModel

app = FastAPI()

class Operation(BaseModel):
    a: float
    b: float

async def request_service(url: str, operation: Operation):
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=operation.dict())
        return response.json()["result"]

@app.post("/add")
async def add(operation: Operation):
    return await request_service("http://localhost:8001/add", operation)

@app.post("/subtract")
async def subtract(operation: Operation):
    return await request_service("http://localhost:8002/subtract", operation)

@app.post("/multiply")
async def multiply(operation: Operation):
    return await request_service("http://localhost:8003/multiply", operation)

@app.post("/divide")
async def divide(operation: Operation):
    return await request_service("http://localhost:8004/divide", operation)
