'''
(Financial application: calculate tips)

Write a program that reads the subtotal and the gratuity rate and computes the gratuity and total. For example, if the user enters 10 for the subtotal and 15% for the gratuity rate, the program displays 1.5 as the gratuity and 11.5 as the total. Here is another sample run:

Enter the subtotal: 15.69

Enter the gratuity rate: 15

The gratuity is 2.35 and the total is 18.04
'''

userSubtotal = float(input("Enter the subtotal: "))
userGratuity = float(input("Enter the gratuity rate: "))
gratuity = userGratuity * 0.01
total = round(((userSubtotal * gratuity) + userSubtotal), 2)
grat = round((gratuity * userSubtotal), 2)
print("The gratuity is " + str(grat) + " and the total is " + str(total))
