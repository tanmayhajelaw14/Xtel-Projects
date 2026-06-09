from calculator_service import CalculatorService

service = CalculatorService()
print(service.calculate(10, 5, "+"))  # Output: 15
print(service.calculate(10, 5, "-"))  # Output: 5   
print(service.calculate(10, 5, "*"))  # Output: 50
print(service.calculate(10, 5, "/"))  # Output: 2.0
