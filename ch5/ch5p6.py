'''
(Business: check ISBN-13)

ISBN-13 is a new standard for indentifying books. It uses 13 digits d1d2d3d4d5d6d7d8d910d11d12d13. The last digit d13 is a checksum, which is calculated from the other digits using the following formula:

10 - (d1 + 3*d2 + d3 + 3*d4 + d5 + 3*d6 + d7 + 3*d8 + d9 + 3*d10 + d11 + 3*d12) % 10

If the checksum is 10, replace it with 0. Your program should read the input as a string. Display “incorrect input” if the input is incorrect.

Sample Run 1

Enter the first 12 digits of an ISBN-13 as a string: 978013213080

The ISBN-13 number is 9780132130806

Sample Run 2

Enter the first 12 digits of an ISBN-13 as a string: 978013213079

The ISBN-13 number is 9780132130790
'''

# 978013213080
num = input("Enter the first 12 digits of an ISBN-13 as a string: ")

check = 0
evens = 0
odds = 0
for i in range(len(num)):
    if i % 2 == 0:
        continue
    odds += int(num[i]) * 3
for i in range(len(num)):
    if i % 2 == 0:
        evens += int(num[i])
check = evens + odds
check = 10 - check % 10
if check == 10:
    check = 0

print("The ISBN-13 number is ",num + str(check))

