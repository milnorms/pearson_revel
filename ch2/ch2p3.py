'''
(Split digits)

Write a program that prompts the user to enter a four-digit integer and displays the number in reverse order. Here is a sample run:

Enter an integer: 5213

3

1

2

5
'''

number = input("Enter an integer: ")
numList = [num for num in number]
for i in reversed(numList) :
    print(i)
