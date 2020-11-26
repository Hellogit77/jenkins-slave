import pytest
import calculator

def test_add():
    assert calculator.add(1, 4) == 5 
def test_subtract():
    assert calculator.subtract(10, 2) == 8
def test_multiply():
    assert calculator.multiply(3, 7) ==21