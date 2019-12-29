'''
(Geometry: area of a regular polygon)

A regular polygon is an n-sided polygon in which all sides are of the same length and all angles have the same degree (i.e., the polygon is both equilateral and equiangular). The formula for computing the area of a regular polygon is

area = (n * s^2) / (4 * tan(PI / n)

Here, s is the length of a side. Write a program that prompts the user to enter the number of sides and their length of a regular polygon and displays its area.

Sample Run

Enter the number of sides: 5

Enter the side: 6.5

The area of the polygon is 72.69017017488385
'''

import math

sides = int(input("Enter the number of sides: "))

length = float(input("Enter the side: "))

PI = math.pi

area = (sides * length**2) / (4 * (math.tan(PI / sides)))

print("The area of the polygon is:", area)
