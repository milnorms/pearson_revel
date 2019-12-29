'''
(Occurrences of a specified character)

Write a function that finds the number of occurrences of a specified character in the string using the following header:

def count(s, ch):

For example, count("Welcome", 'e') returns 2. The str class has the count method. Implement your function without using the count method. Write a test program that reads a string and a character and displays the number of occurrences of the character in the string.


Sample Run

Enter a string: Welcome to Python

Enter a character: o

o appears in Welcome to Python 3 times
'''

def count(s, c):
    ct = 0
    for ch in s:
        if ch == c:
            ct += 1
    return ct
        
s = input("Enter a string: ")
ch = input("Enter a character: ")
print(ch, "appears in", s, count(s, ch), "times")
