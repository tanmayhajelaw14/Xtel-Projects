from abc import ABC, abstractmethod

class OperationStrategy(ABC):
    @abstractmethod
    def calculate(self, a, b):
        pass

class AdditionStrategy(OperationStrategy):
    def calculate(self, a, b):
        return a + b
    

class SubtractionStrategy(OperationStrategy):
    def calculate(self, a, b):
        return a - b


class MultiplicationStrategy(OperationStrategy):
    def calculate(self, a, b):
        return a * b
    
class DivisionStrategy(OperationStrategy):
    def calculate(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
        