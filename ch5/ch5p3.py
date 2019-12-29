'''
(Find the two highest scores)

Write a program that prompts the user to enter the number of students and each student’s name and score, and finally displays the student with the highest score and the student with the second-highest score. Assume that the number of students is at least 2.

Sample Run

Enter the number of students: 5

Enter a student name: Smith

Enter a student score: 60

Enter a student name: Jones

Enter a student score: 96

Enter a student name: Peterson

Enter a student score: 85

Enter a student name: Greenlaw

Enter a student score: 98

Enter a student name: Zhang

Enter a student score: 95

Top two students:

Greenlaw's score is 98.0

Jones's score is 96.0
'''

students = int(input("Enter the number of students: "))
high_name = input("Enter a student name: ")
high_score = int(input("Enter a student score: "))
second_name = input("Enter a student name: ")
second_score = int(input("Enter a student score: "))
current_score = 0
current_name = ""
if second_score > high_score:
    high_score, second_score = second_score, high_score
    high_name, second_name = second_name, high_name
for i in range(students-2):
    current_name = input("Enter a student name: ")
    current_score = int(input("Enter a student score: "))
    if current_score > second_score:
        second_score = current_score
        second_name = current_name
    if second_score > high_score:
        high_score, second_score = second_score, high_score
        high_name, second_name = second_name, high_name
print(high_name, high_score)
print(second_name, second_score)


    

