from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.get("/add/{a}/{b}")
async def add(a: int, b: int):
    return {"result": a + b}
