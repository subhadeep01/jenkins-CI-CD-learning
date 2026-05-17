import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    """Fixture to provide a Calculator instance."""
    return Calculator()

# --- Integration Tests ---
# For a simple Calculator, an integration test can represent a combination of operations
# chaining together to simulate a complex calculation flow.
def test_calculator_integration_workflow(calc):
    """
    Test a complex mathematical expression:
    ((10 + 5) * 2) - (8 / 4) + (3 ** 2)
    = (15 * 2) - 2 + 9
    = 30 - 2 + 9
    = 37
    """
    sum_result = calc.add(10, 5)
    mul_result = calc.mul(sum_result, 2)
    div_result = calc.div(8, 4)
    power_result = calc.power(3, 2)
    
    sub_result = calc.sub(mul_result, div_result)
    final_result = calc.add(sub_result, power_result)
    
    assert final_result == 37.0

# Integration test with main.py conceptually (testing the same calls it makes)
def test_main_script_operations(calc):
    """
    Ensure the specific operations called in main.py work together seamlessly.
    """
    assert calc.add(4, 5) == 9
    assert calc.mul(3, 4) == 12
