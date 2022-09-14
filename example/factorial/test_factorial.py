# content of test_sample.py
from factorial import *
def test_factorial():
    assert factorial(5) == 120
def test_logFactorial():
    assert factorial(5) == round(math.exp(logFactorial(5)))