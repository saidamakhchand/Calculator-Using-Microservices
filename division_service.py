from fastapi import FastAPI

app = FastAPI()

@app.get("/divide/{a}/{b}")
async def divide(a: int, b: int):
    if b == 0:
        return {"error": "Cannot divide by zero"}
    return {"operation": "division", "result": a / b}
