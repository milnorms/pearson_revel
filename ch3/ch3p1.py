'''
(Algebra: solve quadratic equations)

The two roots of a quadratic equation ax^2 + bx + c = 0 can be obtained using the following formula:


r1 = (-b + sqrt(b^2 - 4ac)) / (2a)

and

r2 = (-b - sqrt(b^2 - 4ac)) / (2a)



b^2 - 4ac is called the discriminant of the quadratic equation. If it is positive, the equation has two real roots. If it is zero, the equation has one root. If it is negative, the equation has no real roots.

Write a program that prompts the user to enter values for a, b, and c and displays the result based on the discriminant.

If the discriminant is positive, display two roots.

If the discriminant is 0, display one root.

Otherwise, display “The equation has no real roots”.

Sample Run 1

Enter a: 1.0

Enter b: 3

Enter c: 1

The roots are -0.3819660112501051 and -2.618033988749895

Sample Run 2

Enter a: 1

Enter b: 2.0

Enter c: 1

The root is -1.0

Sample Run 3

Enter a: 1

Enter b: 2

Enter c: 3

The equation has no real roots
'''

# Getting user input for a, b, and c
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# Formula for 2 roots of quadratic equation
r1 = ((-1 * b) + (b * b - 4 * a * c) ** 0.5) / (2 * a)
r2 = ((-1 * b) - (b * b - 4 * a * c) ** 0.5) / (2 * a)

# Getting discriminant
d = (b * b) - 4 * a * c

# If discriminant is positive, display 2 roots, if 0, display
# one root, otherwise, display "The equation has no roots"
if d > 0:
    print("The roots are", str(r1), "and", str(r2))
elif d == 0:
    print("The root is ", str(r1))
else:
    print("The quation has no real roots")
