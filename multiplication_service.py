from fastapi import FastAPI

app = FastAPI()

@app.get("/multiply/{a}/{b}")
async def multiply(a: int, b: int):
    return {"operation": "multiplication", "result": a * b}
