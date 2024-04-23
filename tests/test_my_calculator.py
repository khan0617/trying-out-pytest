import pytest
from my_calculator import MyCalculator

# 4. Pytest fixtures (like @Before in JUnit)
@pytest.fixture
def my_calc_inst() -> MyCalculator:
    return MyCalculator


# 5. showing pytest.raises for catching exceptions
def test_my_calculator_divide_by_zero(my_calc_inst: MyCalculator) -> None:
    with pytest.raises(ZeroDivisionError) as excinfo:
        my_calc_inst.divide(1, 0)


# 6. Skipping a test (note the 's' in the pytest output when we skip the test!)
@pytest.mark.skip(reason="Complex addition not supported yet")
def test_complex_number_add(my_calc_inst: MyCalculator) -> None:
    assert my_calc_inst.complex_add(2 + 3j, 4 + 5j) == 6 + 8j
    