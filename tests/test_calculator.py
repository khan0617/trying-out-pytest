import pytest
from calculator import add, multiply

"""
- First we'll run the system with just 'test_add'.
- Then we'll add test_multiply() and see it fails, show the error message, and fix it.
"""

# 1. run the file with JUST test_add in.
def test_add() -> None:
    assert add(3, 4) == 7


# 2. pytest error messages in the terminal
# def test_multiply() -> None:
#     assert multiply(5, 6) == 30


# 3. pytest parametrization (multiple inputs with one test)
# @pytest.mark.parametrize('a, b, expected', [
#     (1, 1, 2),
#     (5, 6, 11),
#     (-100, -200, -300)
# ])
# def test_add_multiple_values(a: float, b: float, expected: float) -> None:
#     assert add(a, b) == expected

# 7. finally showcase the pytest-cov plugin, run "pytest --cov" in the command line.
