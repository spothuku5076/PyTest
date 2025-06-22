import pytest, time
def add(a,b):
    return a+b

def iseven(n):
    return n%2==0

def is_prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
        
    return count==2


def divide(a,b):
    return a/b

def is_palindrome(s):
    return s==s[::-1]


def add_slow():
    time.sleep(5)
    pass
        
            