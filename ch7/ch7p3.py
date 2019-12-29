'''
(Print distinct numbers)

Write a program that reads in integers separated by a space in one line and displays distinct numbers in their input order and separated by exactly one space (i.e., if a number appears multiple times, it is displayed only once).

Hint: Read all the numbers and store them in list1. Create a new list list2. Add a number in list1 to list2. If the number is already in the list, ignore it.

Sample Run

Enter numbers: 1 2 3 2 1 6 3 4 5 2

The distinct numbers are: 1 2 3 6 4 5
'''

def getInt(string):
    score = string.split(" ")
    for i in range(len(score)):
        score[i] = int(score[i])
    return score


list1 = getInt(input("Enter numbers: "))
list2 = list()
for i in range(len(list1)):
    if list1[i] not in list2:
        list2.append(list1[i])

str1 = ""
for element in list2:
    str1 += str(element)
    str1 += " "
print("The distinct numbers are:", str1)
