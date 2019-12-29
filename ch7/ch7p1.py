'''
(Assign grades)

Write a program that reads a list of scores separated by a space in one line and then assigns grades based on the following scheme:

The grade is A if score is >= best – 10.

The grade is B if score is >= best – 20.

The grade is C if score is >= best – 30.

The grade is D if score is >= best – 40.

The grade is F otherwise.

Sample Run

Enter scores: 40 55 70 58

Student 0 score is 40 and grade is C

Student 1 score is 55 and grade is B

Student 2 score is 70 and grade is A

Student 3 score is 58 and grade is B
'''

def main():
    scores = getScore(input("Enter scores: "))
    grade = getGrade(scores)
    for i in range(len(scores)):
        print("Student", i, "score is", scores[i], "and grade is", grade[i])

def getScore(string):
    score = string.split(" ")
    for i in range(len(score)):
        score[i] = int(score[i])
    return score

def getGrade(scores):
    best = max(scores)
    grades = [None for x in scores]

    for i in range(len(scores)):
        if scores[i] >= best - 10:
            grades[i] = 'A'
        elif scores[i] >= best - 20:
            grades[i] = 'B'
        elif scores[i] >= best - 30:
            grades[i] = 'C'
        elif scores[i] >= best - 40:
            grades[i] = 'D'
        else:
            grades[i] = 'F'
            
    return grades
main()
