'''
(Sorted?)

Write the following function that returns True if the list is already sorted in increasing order:

def isSorted(lst):

Write a test program that prompts the user to enter a list of numbers separated by a space in one line and displays whether the list is sorted or not. Here is a sample run:

Sample Run 1

Enter list: 1 1 3 4 4 5 7 9 10 30 11

The list is not sorted

Sample Run 2

Enter list: 1 1 3 4 4 5 7 9 10 30

The list is already sorted
'''

def main():
    nums = getInt(input("Enter list: "))
    print("The list is already sorted" if isSorted(nums) else "The list is not sorted")

def getInt(string):
    score = string.split(" ")
    for i in range(len(score)):
        score[i] = int(score[i])
    return score

def isSorted(lst):
    s = sorted(lst)
    if s == lst:
        return True
    return False

main()
