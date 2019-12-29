'''
(Geometry: point in a rectangle?)

Write a program that prompts the user to enter a point (x, y) and checks whether the point is within the rectangle centered at (0, 0) with width 10 and height 5. For example, (2, 2) is inside the rectangle and (6, 4) is outside the rectangle, as shown in Figure 3.7b in the Programming Exercise from the Book section.

Hint: A point is in the rectangle if its horizontal distance to (0, 0) is less than or equal to 10 / 2 and its vertical distance to (0, 0) is less than or equal to 5.0 / 2. Test your program to cover all cases.

Sample Run 1

Enter the x-coordinate of the point: 2

Enter the y-coordinate of the point: 2

Point (2.0, 2.0) is in the rectangle

Sample Run 2

Enter the x-coordinate of the point: 6

Enter the y-coordinate of the point: 4

Point (6.0, 4.0) is not in the rectangle
'''

x = float(input("Enter the x-coordinate of the point: "))
y = float(input("Enter the y-coordinate of the point: "))

xrect = x <= 5 and x >= -5
yrect = y <= 2.5 and y >= -2.5

if xrect == True and yrect == True:
    print("Point (",x,",",y,") is in the rectangle")
else:
    print("Point (",x,",",y,") is not in the rectangle")
