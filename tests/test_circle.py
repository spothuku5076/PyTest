from source.circle import Circle, Rectangle
import pytest
from .conftest import *

class TestCircle:
    """This is a test class for Circle"""
    
   #setup_method and teardown_method are special methods recognized by pytest to run before and after each test.

    def setup_method(self):
        print("Setting up the method")

    def teardown_method(self):
        print("Tearing down the method")

    def test_area(self,my_circle):
        # c = Circle(10)
        assert round(my_circle.area(),0) == 314  # use round to avoid floating-point precision issues

    def test_perimeter(self,my_circle):
        # c = Circle(10)
        assert round(my_circle.perimeter(), 1) == 62.8
        
        


def test_area_rectangle(my_rectangle):
    # r = Rectangle(10,20)
    assert my_rectangle.area()==200.0
    
def test_perimeter_rectangle(my_rectangle):
    # r = Rectangle(10,20)
    assert my_rectangle.perimeter()==60.0
