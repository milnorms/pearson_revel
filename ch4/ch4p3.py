'''
(Days of a month)

Write a program that prompts the user to enter the year and the first three letters of a month name (with the first letter in uppercase) and displays the number of days in the month.

Sample Run 1

Enter a year: 2001

Enter a month: Jan

Jan 2001 has 31 days

Sample Run 2

Enter a year: 2000

Enter a month: Feb

Feb 2000 has 29 days

Sample Run 3

Enter a month: 2001

Enter a month: jan

jan is not a correct month name
'''

year = int(input("Enter a year: "))
month = input("Enter a month: ")

isLeapYear = ((year % 4 == 0) and (year % 100 != 0)) or year % 400 == 0

if len(month) == 3 and month[0].isupper():
    if month == "Jan":
        print(month, year, "has 31 days")
    elif month == "Feb":
        print(month, year, "has 29 days" if isLeapYear else "has 28 days")
    elif month == "Mar":
        print(month, year, "has 31 days")
    elif month == "Apr":
        print(month, year, "has 30 days")
    elif month == "May":
        print(month, year, "has 31 days")
    elif month == "Jun":
        print(month, year, "has 30 days")
    elif month == "Jul":
        print(month, year, "has 31 days")
    elif month == "Aug":
        print(month, year, "has 31 days")
    elif month == "Sep":
        print(month, year, "has 30 days")
    elif month == "Oct":
        print(month, year, "has 31 days")
    elif month == "Nov":
        print(month, year, "has 30 days")
    elif month == "Dec":
        print(month, year, "has 31 days")
else:
    print(month, "is not a correct month name")
