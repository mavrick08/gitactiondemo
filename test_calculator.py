from calculator import addition
from calculator import substraction
from calculator import multiplication

def test_add():
    assert addition(10,5) == 15

def test_sub():
    assert substraction(10,5) == 5

def test_mul():
    assert multiplication(2,5) == 14