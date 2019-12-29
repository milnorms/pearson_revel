'''
(Central city)

Given a set of cities, the central point is the city that has the shortest total distance to all other cities. Write a program that prompts the user to enter the locations of the cities (that is, their coordinates), and finds the central city. Note that the coordinates are entered in one line.

Sample Run

Enter the coordinates of the cities: 2.5 5 5.1 3 1 9 5.4 54 5.5 2.1

The central city is at (2.5, 5)
'''

import math
 
def main():
    #s = "2.5 5 5.1 3 1 9 5.4 54 5.5 2.1"
    s = input("Enter the coordinates of the cities: ")
    m = makeCoords(s)
    index = findCentral(m)
    print("The central city is at (" + str(m[index][0]) + ", " + str(m[index][1]) + ")")

def makeCoords(s):
    # returns 2d list of len s // 2 rows and 2 cols
    s = [float(x) for x in s.split()]
    rows = len(s)//2
    cols = 2
    coords = [[0 for i in range(cols)] for j in range(rows)]
    c = 0
    for i in range(rows):
        for j in range(cols):
            coords[i][j] = s[c]
            c += 1
    return coords

def findDistance(a, b):
    # returns float distance between 2 points within 2 lists with 2 elements
    distance = math.sqrt( ((a[0]-b[0])**2)+((a[1]-b[1])**2) )
    return distance

def findCentral(m):
    #takes coords and calculates the distance for every row and compares the total distances for each coordinate to find the shortest one aka CENTRAL
    totals = [0 for x in range(len(m))]
    # print(totals)
    temp = 0
    for i in range(len(m)):
        if temp > 0:
            temp = 0
        for j in range(len(m)):
            temp += findDistance(m[i], m[j])
            totals[i] = temp
    smallest = min(totals)
    index = totals.index(smallest)
    return index

main()
