'''
(Markov matrix)

An n by n matrix is called a positive Markov matrix if each element is positive and the sum of the elements in each column is 1. Write the following function to check whether a matrix is a Markov matrix:

def isMarkovMatrix(m):

Write a test program that prompts the user to enter a 3 by 3 matrix of numbers and tests whether it is a Markov matrix. Note that the matrix is entered by rows and the numbers in each row are separated by a space in one line.

Sample Run 1

Enter a 3-by-3 matrix row by row:

0.15 0.875 0.375

0.55 0.005 0.225

0.30 0.12 0.4

It is a Markov matrix

Sample Run 2

Enter a 3-by-3 matrix row by row:

0.95 -0.875 0.375

0.65 0.005 0.225

0.30 0.22 -0.4

It is not a Markov matrix
'''

def main():
    m = []
    print("Enter a 3-by-3 matrix row by row:")
    for i in range(3):
        s = input("")
        s = [float(x) for x in s.split()]
        m.append(s)
        s = ""
    print("It is a Markov matrix" if isMarkovMatrix(m) else "It is not a Markov matrix")

def isMarkovMatrix(m):
    total = 0
    isMark = False
    for i in range(3):
        total += m[i][0]
        if total == 1:
            isMark = True
            total = 0
    if isMark:
        for i in range(3):
            total += m[i][1]
            if total == 1:
                isMark == True
                total = 0
            else:
                isMark == False
    if isMark:
        for i in range(3):
            total += m[i][2]
            if total == 1:
                isMark == True
                total = 0
            else:
                isMark == False
    return isMark

main()
