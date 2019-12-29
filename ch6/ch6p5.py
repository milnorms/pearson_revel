'''
(Binary to hex)

Write a function that parses a binary number into a hex number. The function header is:

def binaryToHex(binaryValue)

Write a test program that prompts the user to enter a binary number and displays the corresponding hexadecimal value. Use uppercase letters A, B, C, D, E, F for hex digits.

Sample Run

Enter a binary number: 10001111

The hex value is 8F
'''

def binaryToHex(num):
    #binary to decimal conversion
    bins3 = 0
    b = 1
    hexx = ""
    r = 0
    num = "".join(reversed(num))
    # most right is -1 to most left -len(num)
    if num[0] == "1":
        bins3 = 1
    else:
        bins3 == 0
    for i in range(1, len(num)):
        b+= b
        bins3 += int(num[i]) * b
        #print(i, b, num[i], bins3)
    #binary to hexidecimal conversion
    while bins3 > 0:
        r = bins3 % 16
        bins3 = bins3//16
        if r >= 10:
            hexx += hexx.join(chr(55+r))
        elif r < 10:
            hexx += hexx.join(str(r))
        #print(bins3, r)
    hexx = "".join(reversed(hexx))
    print(hexx)


   

num = input("Enter a binary number: ")
binaryToHex(num)
