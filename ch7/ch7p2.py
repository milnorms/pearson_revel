'''
(Count occurrence of numbers)

Write a program that reads some integers between 1 and 100 and counts the occurrences of each. Note that if a number occurs more than one time, the plural word “times” is used in the output. Note the integers are entered in one line separated by a space.

Sample Run

Enter integers between 1 and 100, inclusive: 2 5 6 5 4 3 23 43 2

2 occurs 2 times

3 occurs 1 time

4 occurs 1 time

5 occurs 2 times

6 occurs 1 time

23 occurs 1 time

43 occurs 1 time
'''

def main():
    nums = getInt(input("Enter integers between 1 and 100, inclusive: "))
    count = getCount(nums)
    for i in range(len(count)):
        print(count[i], "occurs", nums.count(count[i]), "time" if nums.count(count[i]) <= 1 else "times")
        
def getInt(string):
    score = string.split(" ")
    for i in range(len(score)):
        score[i] = int(score[i])
    return score

def getCount(nums):
    nums.sort()
    matches = list()
    count = list()
    #print(nums)
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            #print(nums[i], nums[i+1])
            matches.append(nums[i])
            matches.append(nums[i+1])
        else:
            count.append(nums[i])
    if nums[-1] != nums[-2]:
        count.append(nums[-1])
    return count

main()
