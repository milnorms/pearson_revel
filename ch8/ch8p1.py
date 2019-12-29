'''
(Sum elements column by column)

Write a function that returns the sum of all the elements in a specified column in a matrix using the following header:

def sumColumn(m, columnIndex):

Write a test program that reads a 3 × 4 matrix and displays the sum of each column. Note that the matrix is entered by rows and the numbers in each row are separated by a space in one line.

Sample Run

Enter a 3-by-4 matrix row 0: 1.5 2 3 4

Enter a 3-by-4 matrix row 1: 5.5 6 7 8

Enter a 3-by-4 matrix row 2: 9.5 1 3 1

Sum of the elements for column 0 is 16.5

Sum of the elements for column 1 is 9.0

Sum of the elements for column 2 is 13.0

Sum of the elements for column 3 is 13.0
'''

def sumColumn(m, columnIndex):
    s = 0
    for i in range(ROWS):
        s+=m[i][columnIndex]
    return float(s)

m = []
ROWS = 3
COLS = 4


for row in range(ROWS):
    v = (input("Enter a 3-by-4 matrix row "+ str(row) +': '))
    value = [float(x) for x in v.split()]
    m.append(value)

# m = [[1.5, 2, 3, 4], 
#      [5.5, 6, 7, 8], 
#      [9.5, 1, 3, 1]]
for col in range(COLS):
    print("Sum of the elements for column " + str(col) + " is " + str(sumColumn(m, col)))
