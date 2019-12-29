'''
(Split a string)

Write the following function that splits a string into substrings using delimiter characters.

def split(s, delimiters):

For example, split("AB#C D?EF#45", "# ?") returns a list containing AB, C, D, EF, and 45. Write a test program that prompts the user to enter a string and delimiters and displays the substrings separated by exactly one space. (You are not allowed to use the regex for splitting a string in this exercise.)

Sample Run

Enter a string: Welcome to Python

Enter delimiters: oe
W lc m t Pyth n
'''

def main():
    s = input("Enter a string: ")
    d = input("Enter delimiters: ")
    print(split(s, d))
    
def split(s, d):
    dlist = []
    temp = ""
    for i in range(len(d)):
        dlist.append(d[i])
        
    for i in range(len(s)):
        # print(s[i] in dlist)
        if s[i] not in dlist:
            temp += s[i]
        if s[i] in dlist:
            temp += " "
            
    return temp

# s = "he#llo,world"
# d = "#,"
main()

        
