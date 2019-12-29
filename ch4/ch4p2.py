'''
(Convert letter grade to number)

Write a program that prompts the user to enter a letter grade A/a, B/b, C/c, D/d, or F/f and displays its corresponding numeric value 4, 3, 2, 1, or 0.

Sample Run 1

Enter a letter grade: B

The numeric value for grade B is 3

Sample Run 2

Enter a letter grade: b

The numeric value for grade b is 3

Sample Run 3

Enter a letter grade: T

T is an invalid grade
'''

input = input("Enter a letter grade: ")
grade = input.lower()
if grade == 'a':
    print("The numeric value for grade", input, "is 4")
elif grade == 'b':
    print("The numeric value for grade", input, "is 3")
elif grade == 'c':
    print("The numeric value for grade", input, "is 2")
elif grade == 'd':
    print("The numeric value for grade", input, "is 1")
elif grade == 'f':
    print("The numeric value for grade", input, "is 0")
else:
    print(input, "is an invalid grade")
