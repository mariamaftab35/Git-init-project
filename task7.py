
"""Write a program that calculates and prints the value according to the given formula:
Q= Square root of [(2*C*D)/H]
Following are the
"""
import math
c = 50
h = 30
value = []
items = [x for x in input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*(d)/h)))))
print(','.join(value))   

"""
2. Define a class named Shape and its subclass Square. The Square class has an init function which
takes length as argument. Both classes have an area function which can print the area of the shape
where Shape’s area is 0 by default.
"""
class Shape(object):
    def _int_(self):
        pass
    def area(self):
        return 0

class square(Shape):
    def _int_(self,l):
        Shape._int_self
        self.lenght =l
    def area(self):
        return self.length*self.lenght
aSquare = square(3)
print (aSquare.area)        