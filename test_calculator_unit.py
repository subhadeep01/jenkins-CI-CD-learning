import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    """Fixture to provide a Calculator instance."""
    return Calculator()

# --- Unit Tests ---
def test_add(calc):
    assert calc.add(4, 5) == 9
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0

def test_sub(calc):
    assert calc.sub(10, 5) == 5
    assert calc.sub(0, 5) == -5
    assert calc.sub(-5, -5) == 0

def test_mul(calc):
    assert calc.mul(3, 4) == 12
    assert calc.mul(-2, 3) == -6
    assert calc.mul(5, 0) == 0

def test_div(calc):
    assert calc.div(10, 2) == 5.0
    assert calc.div(-10, 2) == -5.0
    
    # Testing division by zero exception
    with pytest.raises(ZeroDivisionError):
        calc.div(5, 0)

def test_power(calc):
    assert calc.power(2, 3) == 8
    assert calc.power(5, 0) == 1
    assert calc.power(2, -1) == 0.5
