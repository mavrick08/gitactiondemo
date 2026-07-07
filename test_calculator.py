from calculator import addition
from calculator import substraction

def test_add():
    assert addition(10,5) == 15

def test_sub():
    assert substraction(10,5) == 5