#another example of using special method 
#through vector multiplication 

import math

class Vector:

    def __init__(self,x=0,y=0): 
        self.x = x
        self.y = y 

    def __repr__(self): # this is repr built in function, which return printable string of any given object 
        return f'Vector({self.x!r},{self.y!r})'

    def __abs__(self):
        return math.hypot(self.x,self.y)

    def __bol__(self):
        return bool(abs(self))

    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)
    
    def __mul__(self,scalar):
        return Vector(self.x*scalar, self.y*scalar)

wow = Vector(1,2)
