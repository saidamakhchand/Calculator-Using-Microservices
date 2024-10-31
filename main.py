from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# إعداد CORS
origins = [
    "http://localhost:5500",  # أو استخدم "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # تأكد من أنها مضافة بشكل صحيح
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CalculationRequest(BaseModel):
    expression: str

@app.get("/calculate")
async def calculate(expression: str):
    try:
        # استخدم eval بحذر أو مكتبة للعمليات الحسابية
        result = eval(expression)
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
