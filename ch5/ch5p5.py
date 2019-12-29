'''
(Count vowels and consonants)

Assume letters A, E, I, O, and U as the vowels. Write a program that prompts the user to enter a string and displays the number of vowels and consonants in the string.

Sample Run

Enter a string: Programming is fun

The number of vowels is 5

The number of consonants is 11
'''

word = input("Enter a string: ")
const = 0
vowel = 0
for ch in word:
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        vowel += 1
    elif ch.isalpha() and (ch != 'a' or ch != 'e' or ch != 'i' or ch != 'o' or ch != 'u'):
        const += 1
print("The number of vowels is", vowel)
print("The number of consonants is", const)
