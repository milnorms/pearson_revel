'''
See Exercise 8.5 in Chapter 8 Programming Exercise from the Book section for this project.
write a funciton to add 2 matricies
'''

def main():
    s = input("Enter a 3-by-3 matrix1: ")
    m1 = make3x3Matrix(s)
    s1 = input("Enter a 3-by-3 matrix1: ")
    m2 = make3x3Matrix(s1)
    print(addMatrix(m1, m2))

def addMatrix(a, b):
    r = []
    for i in range(3):
        r.append([])
        for j in range(3):
            r[i].append(0)
            r[i][j] = a[i][j] + b[i][j]
    return r

def make3x3Matrix(s):
    m1 = []
    s = [float(x) for x in s.split()]
    m1.append(s[0:3])
    m1.append(s[3:6])
    m1.append(s[6:10])
    return m1

main()
