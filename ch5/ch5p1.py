'''
(Count positive and negative numbers and compute the average of numbers)

Write a program that reads an unspecified number of integers, determines how many positive and negative values have been read, and computes the total and average of the input values (not counting zeros). Your program ends with the input 0. Display the average as a floating-point number.

Sample Run 1

﻿Sample Output 1:

Enter an integer, the input ends if it is 0: 1

Enter an integer, the input ends if it is 0: 2

Enter an integer, the input ends if it is 0: -1

Enter an integer, the input ends if it is 0: 3

Enter an integer, the input ends if it is 0: 0

The number of positives is 3

The number of negatives is 1

The total is 5

The average is 1.25

Sample Run 2

﻿Sample Output 2:

Enter an integer, the input ends if it is 0: 0

No numbers are entered except 0
'''

num = int(input("Enter an integer, the input ends if it is 0: "))
pos = 0
neg = 0
count = 0
tot = num
if num > 0:
    pos+=1
elif num < 0:
    neg+=1
elif num == 0:
    print("No numbers are entered except 0")
    quit()

while num != 0:
    num = int(input("Enter an integer, the input ends if it is 0: "))
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
    count += 1
    tot += num
avg = tot/ count
print("The number of positives is: ", pos)
print("The number of negatives is: ", neg)
print("The total is", tot)
print("The average is", avg)
