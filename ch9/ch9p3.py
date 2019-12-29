'''
(The Point class)

Design a class named Point to represent a point with x- and y-coordinates. The class contains:

- Two private data fields x and y that represent the coordinates with getter methods.
- A constructor that constructs a point with specified coordinates, with default(0, 0).
- A method named distance that returns the distance from this point to another point of the Point type.
- A method named isNearBy(p1) that returns True if point p1 is close to this point. Two points are close if their distance is less than 5.
- Implement the __str__ method to return a string in the form (x, y).

Draw the UML diagram for the class, and then implement the class. Write a test program that prompts the user to enter two points, displays the distance between them, and indicates whether they are near each other.


Sample Run 1

Enter the x-coordinate of point1: 2.1

Enter the y-coordinate of point1: 2.3

Enter the x-coordinate of point2: 19.1

Enter the y-coordinate of point2: 19.2

The distance between the two points is 23.97

The two points are not near to other

Sample Run 2

Enter the x-coordinate of point1: 2.1

Enter the y-coordinate of point1: 2.3

Enter the x-coordinate of point2: 2.3

Enter the y-coordinate of point2: 4.2

The distance between the two points is 1.91

The two points are near to other
'''

def main():
    x1 = float(input("Enter the x-coordinate of point1: "))
    y1 = float(input("Enter the y-coordinate of point1: "))
    x2 = float(input("Enter the x-coordinate of point2: "))
    y2 = float(input("Enter the y-coordinate of point2: "))
    
    # x1 = 2.1
    # y1 = 2.3
    # x2 = 2.3
    # y2 = 4.2
    
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    print("The distance between the two points is ", round(p1.distance(p2), 2))
    print("The two points are near to other" if p1.isNearBy(p2) else "The two points are not near to other")

class Point:
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y
        
    def getX(self):
        return self.__x
        
    def getY(self):
        return self.__y
    
    def distance(self, p1):
        x1 = self.__x
        y1 = self.__y
        x2 = p1.getX()
        y2 = p1.getY()
        return ((x2 - x1)**2 + (y2 - y1)**2 )**0.5
        
    
    def isNearBy(self, p1):
        if self.distance(p1) < 5:
            return True
        return False
    
    def __str__(self):
        return "(" + str(self.__x) + "," + str(self.__y) + ")"

main()
