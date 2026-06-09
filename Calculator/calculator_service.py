from strategies import AdditionStrategy, SubtractionStrategy, MultiplicationStrategy, DivisionStrategy


class CalculatorService:
    def calculate(self,num1,num2,operation):
        strategies = {
            "+": AdditionStrategy(),
            "-": SubtractionStrategy(),
            "*": MultiplicationStrategy(),
            "/": DivisionStrategy()

        }
        strategy = strategies.get(operation)
        
        if not strategy:
            raise ValueError("Invalid operation")
        
        return strategy.calculate(num1,num2)
    