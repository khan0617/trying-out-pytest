import pytest
from my_calculator import MyCalculator

# 4. Pytest fixtures (like @Before in JUnit)
# @pytest.fixture
# def myCalcInst() -> MyCalculator:
#     return MyCalculator


# 5. showing pytest.raises for catching exceptions
# def test_my_calculator_divide_by_zero(myCalcInst: MyCalculator) -> None:
#     with pytest.raises(ZeroDivisionError) as excinfo:
#         myCalcInst.divide(1, 0)


# 6. Skipping a test (note the 's' in the pytest output when we skip the test!)
# @pytest.mark.skip(reason="Complex addition not supported yet")
# def test_complex_number_add(myCalcInst: MyCalculator) -> None:
#     assert myCalcInst.complexAdd(2 + 3j, 4 + 5j) == 6 + 8j
    