'''
(Locate the largest element)

Write the following function that returns the location of the largest element in a two-dimensional list:

def locateLargest(a):

The return value is a one-dimensional list that contains two elements. These two elements indicate the row and column indexes of the largest element in the two-dimensional list. Write a test program that prompts the user to enter a two-dimensional list and displays the location of the largest element in the list. Note that the matrix is entered by rows and the numbers in each row are separated by a space in one line. Here is a sample run:

Sample Run

Enter the number of rows in the list: 3

Enter a row: 23.5 35 2 10

Enter a row: 4.5 3 45 3.5

Enter a row: 35 44 5.5 11.6

The location of the largest element is at (1, 2)
'''

def main():
    rows = int(input("Enter the number of rows in the list: "))
    l = []
    m = []
    for i in range(rows):
        s = input("Enter a row: ")
        l = [float(x) for x in s.split()]
        m.append(l)
    loclrg = ""
    for i in range(len(locateLargest(m))):
        loclrg += str(locateLargest(m)[i])
        if len(loclrg) < 2:
            loclrg += ", "
    print("The location of the largest element is at " + "(" + loclrg + ")")
    
def locateLargest(m):
    rows = len(m)
    cols = len(m[0])
    index = [0 for x in range(2)]
    lrg = m[0][0]
    for i in range(rows):
        for j in range(cols):
            if m[i][j] > lrg:
                lrg = m[i][j]
                index[0] = i
                index[1] = j
    
    return index

main()
