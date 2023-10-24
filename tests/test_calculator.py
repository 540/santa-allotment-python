from assertpy import assert_that
from src.calculator import add, multiply

def test_adds_two_numbers():
    assert_that(add(1, 2)).is_equal_to(3)
    
def test_multiply_two_numbers():
    assert_that(multiply(1, 2)).is_equal_to(2)