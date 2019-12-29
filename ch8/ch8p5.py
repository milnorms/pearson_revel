'''
(Column sorting)

Implement the following function to sort the columns in a two-dimensional list. A new list is returned and the original list is intact.

def sortColumns(m):

Write a test program that prompts the user to enter a 3 by 3 matrix of numbers and displays a new column-sorted matrix. Note that the matrix is entered by rows and the numbers in each row are separated by a space in one line.

Sample Run

Enter a 3-by-3 matrix row by row:

0.15 0.875 0.375

0.55 0.005 0.225

0.30 0.12 0.4

The column-sorted list is

0.15 0.005 0.225

0.3 0.12 0.375

0.55 0.875 0.4
'''


###NEW PROJECT

def sortCols(m):
    sort = [[0 for i in range(3)] for x in range(3)]

    temp = []

    for j in range(len(m[0])):
        for i in range(len(m)):
                if j == 0:
                    temp.append(m[i][j])
                    temp.sort()

    for j in range(len(m[0])):
        for i in range(len(m)):
            if j == 0:
                sort[i][j] = temp[i]
    temp = []

    for j in range(len(m[0])):
        for i in range(len(m)):
                if j == 1:
                    temp.append(m[i][j])
                    temp.sort()

    for j in range(len(m[0])):
        for i in range(len(m)):
            if j == 1:
                sort[i][j] = temp[i]
    temp = []

    for j in range(len(m[0])):
        for i in range(len(m)):
                if j == 2:
                    temp.append(m[i][j])
                    temp.sort()

    for j in range(len(m[0])):
        for i in range(len(m)):
            if j == 2:
                sort[i][j] = temp[i]
    temp = []

    return sort

# m = [[3, 1, 3], 
#     [1, 19, 6], 
#     [7, 2, 1]]


m = []
print("Enter a 3-by-3 matrix row by row:")
for i in range(3):
    s = input("")
    s = [float(x) for x in s.split()]
    m.append(s)
    s = ""
print(sortCols(m))




        


