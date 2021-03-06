# AUTOGENERATED! DO NOT EDIT! File to edit: 00_core.ipynb (unless otherwise specified).

__all__ = ['Circle']

# Cell
import math
class Circle:
    '''This is a sample class to get properties of a cricle'''
    def __init__(self,r:float):
        self.r = r
    @property
    def perimeter(self):
        """returns the perimeter of the circle"""
        return 2 * math.pi * self.r
    @property
    def area(self):
        """returns the area of the circle"""
        return math.pi * (self.r)**2
