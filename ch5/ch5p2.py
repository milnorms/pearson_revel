'''
(Financial application: compute future tuition)

Suppose that the tuition for a university is $10,000 this year and increases 5% every year. In one year, the tuition will be $10,500. Write a program that displays the tuition in 10 years and the total cost of 4 years’ worth of tuition starting after the 10th year.
'''

#Suppose that the tuition for a university is $10,000 
#this year and increases 5% every year. In one year, 
#the tuition will be $10,500. Write a program that displays 
#the tuition in 10 years and the total cost of 4 years’ worth 
#of tuition starting after the 10th year.

import math
tuition = 10000
INCREASE = 1.05
years = 10
for i in range(years):
    tuition *= INCREASE
ten = tuition
four = tuition

final = 0
for i in range(10,14):
     final += (10000*pow(1.05,i))

print(ten)
print(final)



    
