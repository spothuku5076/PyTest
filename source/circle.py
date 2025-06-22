import math
class Shape:
    """This is about general shapes"""
    def __init__(self):
        pass
    def area(self):
        pass
    def perimeter(self):
        pass
    
    
class Circle(Shape):
    """This is about a circle"""
    def __init__(self, radius):
        self.radius=radius
    
    def area(self):
        return math.pi*self.radius**2
    
    def perimeter(self):
        return 2 * math.pi*self.radius
    
    
class Rectangle(Shape):
    """_summary_

    Args:
        Shape (_type_): _description_
    """
    def __init__(self, l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l * self.b
    def perimeter(self):
        return 2*(self.l+self.b)
    
    
    