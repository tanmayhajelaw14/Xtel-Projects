from fastapi import FastAPI
from pydantic import BaseModel
from calculator_service import CalculatorService


app = FastAPI()
service = CalculatorService() 

class CalculationRequest(BaseModel):
    num1: float
    num2: float
    operation: str


@app.get("/")
def home():
    return {"message": "Welcome to the Calculator API!"}

@app.post("/calculate")
def calculate(request: CalculationRequest):

    result = service.calculate(request.num1, request.num2, request.operation)   
    return {"result": result}