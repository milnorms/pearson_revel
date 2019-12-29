'''
(Science: day of the week)

Zeller’s congruence is an algorithm developed by Christian Zeller to calculate the day of the week. The formula is

h = (q + 26(m+1)//10 + k + k//4 +j//4 +5j) % 7

where

- h is the day of the week (0: Saturday, 1: Sunday, 2: Monday, 3: Tuesday, 4: Wednesday, 5: Thursday, 6: Friday).
- q is the day of the month.
- m is the month (3: March, 4: April, ..., 12: December). January and February are counted as months 13 and 14 of the previous year.
- j is year//100.
- k is the year of the century (i.e., year % 100).


Write a program that prompts the user to enter a year, month, and day of the month, and then it displays the name of the day of the week.

Sample Run 1

Enter year: (e.g., 2008): 2013

Enter month: 1-12: 1

Enter the day of the month: 1-31: 25

Day of the week is Friday

Sample Run 2

Enter year: (e.g., 2008): 2012

Enter month: 1-12: 5

Enter the day of the month: 1-31: 12

Day of the week is Saturday

Hint: Use the // operator for integer division. January and February are counted as 13 and 14 in the formula, so you need to convert the user input 1 to 13 and 2 to 14 for the month and change the year to the previous year.
'''


year = int(input("Enter year: (e.g., 2008): "))
month = int(input("Enter month: 1 - 12: "))
day = int(input("Enter day of the month: 1 - 31: "))

if month == 1:
    month = 13
    year -= 1
elif month == 2:
    month = 14
    year -= 1

j = year // 100
k = year % 100

h = (day + (26*month+(26*1))//10 + k + k//4 +j//4 +5*j) % 7

if h == 0:
    print("Day of the week is Saturday")
elif h == 1:
    print("Day of the week is Sunday")
elif h == 2:
    print("Day of the week is Monday")
elif h == 3:
    print("Day of the week is Tuesday")
elif h == 4:
    print("Day of the week is Wednesday")
elif h == 5:
    print("Day of the week is Thursday")
elif h == 6:
    print("Day of the week is Friday")
