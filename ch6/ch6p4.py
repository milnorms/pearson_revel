'''
(Convert milliseconds to hours, minutes, and seconds)

Write a function that converts milliseconds to hours, minutes, and seconds using the following header:

def convertMillis(millis):

The function returns a string as hours:minutes:seconds.

For example, convertMillis(5500) returns the string 0:0:5, convertMillis(100000) returns the string 0:1:40, and convertMillis(555550000) returns the string 154:19:10.

Write a test program that prompts the user to enter a value for milliseconds and displays a string in the format of hours:minutes:seconds.

Sample Run

Enter time in milliseconds: 555550000

154:19:10
'''

def convertMillis(millis):
    sec = mil /1000
    secs  = sec % 60
    minutes = sec / 60
    minss = minutes % 60
    hours = minutes / 60
    if hours <= 0:
        hours = 0
    elif minss <= 0:
        minss = 0
    elif secs <= 0:
        secs = 0
    time = str(int(hours)) + ":" + str(int(minss)) + ":" + str(int(secs))
    print(time)
mil = int(input("Enter time in milliseconds: "))
convertMillis(mil)
