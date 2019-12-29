'''
(Find the number of days in a month)

Write a program that prompts the user to enter the month and year and displays the number of days in the month. For example, if the user entered month 2 and year 2000, the program should display that February 2000 has 29 days. If the user entered month 3 and year 2005, the program should display that March 2005 has 31 days.

Sample Run 1

Enter a month in the year (e.g., 1 for Jan): 4

Enter a year: 2005

April 2005 has 30 days

Sample Run 2

Enter a month in the year (e.g., 1 for Jan): 2

Enter a year: 2006

February 2006 has 28 days

Sample Run 3

Enter a month in the year (e.g., 1 for Jan): 2

Enter a year: 2000

February 2000 has 29 days
'''
## project 3

month = int(input("Enter a month in the year (e.g., 1 for Jan: ) "))
year = int(input("Enter a year: "))
isLeapYear = ((year % 4 == 0) and (year % 100 != 0)) or year % 400 == 0



if month == 1:
    print("January", year, "has 31 days")
elif month == 2:
    print("February", year, "has 29 days" if isLeapYear else "has 28 days")
elif month == 3:
    print("March", year, "has 31 days")
elif month == 4:
    print("April", year, "has 30 days")
elif month == 5:
    print("May", year, "has 31 days")
elif month == 6:
    print("June", year, "has 30 days")
elif month == 7:
    print("July", year, "has 31 days")
elif month == 8:
    print("August", year, "has 31 days")
elif month == 9:
    print("September", year, "has 30 days")
elif month == 10:
    print("October", year, "has 31 days")
elif month == 11:
    print("November", year, "has 30 days")
elif month == 12:
    print("December", year, "has 31 days")
