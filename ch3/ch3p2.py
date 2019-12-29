'''
(Algebra: solve 2 × 2 linear equations)

You can use Cramer’s rule to solve the following 2 × 2 system of linear equation:

ax + by = e

cx + dy = f

x = (ed - bf) / (ad - bc)

y = (af -ec) / (ad - bc)

Write a program that prompts the user to enter a, b, c, d, e, and f and display the result. If ad - bc is 0, report that “The equation has no solution.”

Sample Run 1

Enter a: 9.0

Enter b: 4.0

Enter c: 3.0

Enter d: -5.0

Enter e: -6.0

Enter f: -21.0

x is -2.0 and y is 3.0

Sample Run 2

Enter a: 1.0

Enter b: 2.0

Enter c: 2.0

Enter d: 4.0

Enter e: 4.0

Enter f: 5.0

The equation has no solution
'''


a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
d = float(input("Enter d: "))
e = float(input("Enter e: "))
f = float(input("Enter f: "))



if ((a * d) - (b * c)) == 0:
    print("The equation has no solution")
else:
    x = ((e * d) - (b * f)) / ((a * d) - (b * c))
    y = ((a * f) - (e * c)) / ((a * d) - (b * c))
    print("x is", str(x), "and y is", str(y))
