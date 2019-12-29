'''
See Exercise 9.15 in the Chapter 9 Programming Exercise from the Book section for the description of this exercise.​

Sample Run

Enter the real part of the first complex number: 3.5

Enter the imaginary part of the first complex number: 6.5

Enter the real part of the second complex number: -3.5

Enter the imaginary part of the second complex number: 1

(3.5 + 6.5i) + (-3.5 + 1i) = (0.0 + 7.5i)

(3.5 + 6.5i) - (-3.5 + 1i) = (7.0 + 5.5i)

(3.5 + 6.5i) * (-3.5 + 1i) = (-18.75 - 19.25i)

(3.5 + 6.5i) / (-3.5 + 1i) = (-0.43396226415 - 1.98113207547i)

|(3.5 + 6.5i)| = 7.3824115301167
'''

def main():
    a1 = float(input("Enter the real part of the first complex number: "))
    b1 = float(input("Enter the imaginary part of the first complex number: "))
    a2 = float(input("Enter the real part of the second complex number: "))
    b2 = float(input("Enter the imaginary part of the second complex number: "))
    
    c1 = Complex(a1, b1)
    c2 = Complex(a2, b2)
    # c1 = Complex(3.5, 6.5)
    # c2 = Complex(-3.5, 1)
    print(c1, "+", c2, "=", c1+c2)
    print(c1, "-", c2, "=", c1-c2)
    print(c1, "*", c2, "=", c1*c2)
    print(c1, "/", c2, "=", c1/c2)
    print("|", c1, "|", "=", abs(c1))

    
class Complex:
    def __init__(self, a = 0, b = 0):
        self.__a = a
        self.__b = b
    
    def getRealPart(self):
        return self.__a
    
    def getImaginaryPart(self):
        return self.__b
        
    def __str__(self):

        return "(" + str(self.__a) + " "+ "+" + " " + str(self.__b) + "i" + ")"
        # return "(" + str(self.__a) + " "+ "-" + " " + str(self.__b * -1) + "i" + ")"
    
    def __add__(self, c2):
        a1 = self.__a + c2.getRealPart()
        b1 = self.__b + c2.getImaginaryPart()
        return Complex(a1, b1)
    
    def __sub__(self, c2):
        a1 = self.__a - c2.getRealPart()
        b1 = self.__b - c2.getImaginaryPart()
        return Complex(a1, b1)
    
    def __mul__(self, c2):
        a1 = (self.__a * c2.getRealPart()) - (self.__b * c2.getImaginaryPart())
        b1 = (self.__b * c2.getRealPart()) + (self.__a * c2.getImaginaryPart())
        return Complex(a1, b1)
    
    def __truediv__(self, c2):
        a1 = ((self.__a * c2.getRealPart()) + (self.__b * c2.getImaginaryPart())) / (c2.getRealPart()**2 + c2.getImaginaryPart()**2)
        a2 = ((self.__b * c2.getRealPart()) - (self.__a * c2.getImaginaryPart())) / (c2.getRealPart()**2 + c2.getImaginaryPart()**2)
        return Complex(round(a1, 11), round(a2, 11))
        
    def __abs__(self):
        return (self.__a**2 + self.__b**2)**0.5

main()
        


# c1 = Complex(3.5, 6.5)
# c2 = Complex(-3.5, 1)
# print(c1 + c2, c1 - c2, c1 * c2, c1 / c2, abs(c1))
