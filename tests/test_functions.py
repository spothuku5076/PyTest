from source.functions import *
import pytest


def test_add():
    assert add(1,3)==4
    

def test_iseven_even():
    assert iseven(2)==True

def test_iseven_odd():
    assert iseven(3)==False
    
def test_is_prime_prime():
    assert is_prime(2)==True
    
def test_is_prime_not_prime():
    assert is_prime(6)==False
    
def test_divide():
    assert divide(10,2)==5
    
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10,0)
        
@pytest.mark.skip(reason="This feature is currently broken")
@pytest.mark.string
def test_is_palindrome_palindrome():
    assert is_palindrome("madam")==True
    
    
@pytest.mark.string 
def test_is_palindrome_not_palindrome():
    assert is_palindrome("Lalitesh")==False
    
@pytest.mark.slow
def test_slow():
    pass


@pytest.mark.xfail(reason="We cannot divide by zero")
def test_divide_by_zero():
    with pytest.raises("Zero division error"):
        divide(4,0)
        

# test multiple inputs
@pytest.mark.parametrize("input,expected",[("madam",True),("lalitesh", False),("hari",False),("malayalam",True)])
def test_is_palindrome_palindrome(input,expected):
    assert is_palindrome(input)==expected

