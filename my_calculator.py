# step 3: use the MyCalculator class to demonstrate:
#   - pytest fixtures (like @Before)
#   - pytest.raises
class MyCalculator:
    def add(a: float, b: float) -> float:
        return a + b
    
    def subtract(a: float, b: float) -> float:
        return a - b
    
    def multiply(a: float, b: float) -> float:
        return a * b
    
    def divide(a: float, b: float) -> float:
        return a / b
    