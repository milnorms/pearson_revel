'''
(Financial application: compare loans with various interest rates)

Write a program that lets the user enter the loan amount and loan period in number of years and displays the monthly and total payments for each interest rate starting from 5% to 8%, with an increment of 1/8.

Sample Run
Loan Amount: 10000

Number of Years: 5

Interest Rate Monthly Payment Total Payment

5.000% 188.71 11322.74

5.125% 189.29 11357.13

5.250% 189.86 11391.59

...

7.875% 202.17 12129.97

8.000% 202.76 12165.84

For the formula to compute monthly payment, see LiveExample 2.8, ComputeLoan.py.
'''

loan = (input("Loan Amount: "))
loan = float(loan)
years = int(input("Number of Years: "))
interest = 4.875 # starting from 5 - .125 to display the 5 in loop
monthly_intrest = 0
monthly_payment = 0
total = 0
display_interest = 0
print("Interest Rate Monthly Payment Total Payment")
while interest < 8:
    interest += .125
    display_interest = interest/100
    monthly_intrest = interest/1200
    monthly_payment = loan * monthly_intrest / (1-1 /(1 + monthly_intrest) ** (years * 12))
    total = (monthly_payment * 12) * years
    print(format(display_interest, "1.3%"), round(monthly_payment, 2), round(total, 2))
