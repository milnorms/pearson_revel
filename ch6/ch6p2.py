'''
(Financial application: compute the future investment value)

Write a function that computes a future investment value at a given interest rate for a specified number of years. The future investment is determined using the formula in Programming Exercise 2.19 in Chapter 2 Programming Exercise from the Book.

Use the following function header:

def futureInvestmentValue(investmentAmount, monthlyInterestRate, years):

For example, futureInvestmentValue(10000, 0.05/12, 5) returns 12833.59.

Write a test program that prompts the user to enter the investment amount and the annual interest rate in percent and prints a table that displays the future value for the years from 1 to 30.

Sample Run

The amount invested: 1000
Annual interest rate: 9

Years Future Value

1 1093.80

2 1196.41

...

29 13467.25

30 14730.58
'''

def futureInvestmentValue(investmentAmount, monthlyInterestRate, years):
    numberOfMonths = years * 12
    futureInvestmentAmount =  investmentAmount * ((1 + monthlyInterestRate) ** numberOfMonths)
    return futureInvestmentAmount

investment = int(input("The amount invested: "))
annual_interest = float(input("Annual interest rate: "))
interest = annual_interest / 100
print("Years Future Value")
for i in range(1, 31):
    print(i, format(futureInvestmentValue(investment, interest/12, i), "0.2f"))
