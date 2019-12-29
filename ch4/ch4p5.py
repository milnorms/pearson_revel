'''
(Hex to binary)

Write a program that prompts the user to enter a hex digit and displays its corresponding binary number.

Sample Run 1
Enter a hex digit: B

The binary value is 1011

Sample Run 2

Enter a hex digit: b

The binary value is 1011

Sample Run 3

Enter a hex digit: T

Invalid input
'''

hex = input("Enter a hex digit: ")
hex = hex.upper()
if hex == 'A':
    print("The binary value is 1010")
elif hex == 'B':
    print("The binary value is 1011")
elif hex == 'C':
    print("The binary value is 1100")
elif hex == 'D':
    print("The binary value is 1101")
elif hex == 'E':
    print("The binary value is 1110")
elif hex == 'F':
    print("The binary value is 1111")
elif hex == "0":
    print("The binary value is 0000")
elif hex == "1":
    print("The binary value is 0001")
elif hex == "2":
    print("The binary value is 0010")
elif hex == "3":
    print("The binary value is 0011")
elif hex == "4":
    print("The binary value is 0100")
elif hex == "5":
    print("The binary value is 0101")
elif hex == "6":
    print("The binary value is 0110")
elif hex == "7":
    print("The binary value is 0111")
elif hex == "8":
    print("The binary value is 1000")
elif hex == "9":
    print("The binary value is 1001")
else:
    print("Invalid input")
