from fastapi import FastAPI

app = FastAPI()

@app.get("/subtract/{a}/{b}")
async def subtract(a: int, b: int):
    return {"operation": "subtraction", "result": a - b}
