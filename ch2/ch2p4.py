'''
(Slope of a line)

Write a program that prompts the user to enter the coordinates of two points (x1, y1) and (x2, y2), and displays the slope of the line that connects the two points. The formula of the slope is (y2 - y1) / (x2 - x1). Here is a sample run:

Enter the x-coordinate for point1: 4.5

Enter the y-coordinate for point1: -5.5

Enter the x-coordinate for point2: 6.6

Enter the y-coordinate for point2: -6.5

The slope for the line that connects two points (4.5, -5.5) and (6.6, -6.5) is -0.47619
'''

oneX = float(input("Enter the x-coordinate for point1: "))
oneY = float(input("Enter the y-coordinate for point1: "))
twoX = float(input("Enter the x-coordinate for point2: "))
twoY = float(input("Enter the y-coordinate for point2: "))
y = twoY - oneY
x = twoX - oneX
final = y / x
print("The slope for the line that connects two points (" + str(oneX) + ", " + str(oneY) + ") and (" + str(twoX) + ", " + str(twoY) + ") is " + str(round(final, 5)))
