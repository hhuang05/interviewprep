#!/usr/bin/env python3

from math import hypot

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Returns a representation that can be passed to eval
    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    # Called by interpreter when using math.abs(<vector>)
    def __abs__(self):
        return hypot(self.x, self.y)

    # Allows interpreter to interrogate object if it is a vector
    # of length 0
    def __bool__(self):
        return bool(self.x or self.y)

    # Overloads + operator to add two vectors
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)

    # Overloads * oeprator to multiply by scalar
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
