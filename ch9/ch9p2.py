'''
(Geometry: n-sided regular polygon)

An n-sided regular polygon’s sides all have the same length and all of its angles have the same degree (i.e., the polygon is both equilateral and equiangular). Design a class named RegularPolygon that contains:

- A private int data field named n that defines the number of sides in the polygon.
- A private float data field named side that stores the length of the side.
- A private float data field named x that defines the x-coordinate of the center of the polygon with default value 0.
- A private float data field named y that defines the y-coordinate of the center of the polygon with default value 0.
- A constructor that creates a regular polygon with the specified n (default 3), side (default 1), x (default 0), and y (default 0).
- The accessor and mutator methods for all data fields.
- The method getPerimeter() that returns the perimeter of the polygon.
- The method getArea() that returns the area of the polygon. The formula for computing the area of a regular polygon is area = (n * s^2) / (4 * tan(PI / n)).

Draw the UML diagram for the class, and then implement the class.

Write a test program that creates three RegularPolygon objects, created using RegularPolygon(), RegularPolygon(6, 4) and RegularPolygon(10, 4, 5.6, 7.8). For each object, display its perimeter and area.
'''

import math

class RegularPolygon:
    def __init__(self, n = 3, side = 1, x = 0, y = 0, ):
        self.__n = n
        self.__side = side
        self.__x = x
        self.__y = y
        
    def getNumSides(self):
        return self.__n
        
    def getSides(self):
        return self.__side
        
    def getX(self):
        return self.__x
        
    def getY(self):
        return self.__y
    
    def setNumSides(self, n):
        self.__n = n
    
    def setSides(self, side):
        self.__side = side
    
    def setX(self, x):
        self.__x = x
        
    def setY(self, y):
        self.__y = y
        
    def getPerimeter(self):
        p = 0
        for i in range(self.__n):
            p += self.__side
        return p
        
    def getArea(self):
        # area = (n * s^2) / (4 * tan(PI / n)).
        a = 0
        a = (self.__n * self.__side**2) / (4 * math.tan(math.pi / self.__n))
        return a 

r1 = RegularPolygon()
r2 = RegularPolygon(6, 4)
r3 = RegularPolygon(10, 4, 5.6, 7.8)
print(r1.getPerimeter(), r1.getArea(), r2.getPerimeter(), r2.getArea(), r3.getPerimeter(), r3.getArea())

        
