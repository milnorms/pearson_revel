'''
See Exercise 7.9 in Chapter 7 Programming Exercise from the Book for the description.

Sample Run

Enter numbers: 1.9 2.5 3.7 2 1 6 3 4 5 2

The mean is 3.11

The standard deviation is 1.55738
'''

def findN(nums):
    count = 0
    for item in nums:
        count += 1
    return count

def mean(nums):
    total = 0
    count = findN(nums)
    for element in nums:
        total += element
    mean = total / count
    return mean


def deviation(nums, mean):
    dif = 0
    comp = []
    total = 0
    n = findN(nums) - 1
    div = 0 
    sqrt = 0
    for i in range(len(nums)):
        dif = nums[i] - mean
        if dif < 0:
            dif = dif * -1
        dif *= dif
        comp.append(dif)
        dif = 0
    for element in comp:
        total += element
    div = total / n
    sqrt = div ** 0.5
    return sqrt

def getFloat(string):
    score = string.split(" ")
    for i in range(len(score)):
        score[i] = float(score[i])
    return score

nums = getFloat(input("Enter numbers: "))
mean = mean(nums)
dev = deviation(nums, mean)
print("The mean is:", mean)
print("The standard deviation is:", dev)

'''
book's solution:

port math
def main():
    # Read numbers as a string from the console
    s = input("Enter numbers: ") 
    items = s.split() # Extracts items from the string
    numbers = [float(x) for x in items] # Convert items to numbers
    # Display mean and deviation
    print("The mean is", mean(numbers))
    print("The standard deviation is", deviation(numbers))
# Compute the deviation of values
def deviation(x):
    average = mean(x)
    squareSum = 0
    for value in x:
      squareSum += (value - average) ** 2
    return math.sqrt(squareSum / (len(x) - 1))
# Compute the mean of a list of values
def mean(x):
    sum = 0
    for value in x:
      sum += value
    return sum / len(x)
main()

''''
