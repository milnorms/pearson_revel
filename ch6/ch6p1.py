'''
(Sum series)

Write a function to compute the following series:

m(i) = 1/2 + 2/3 + ... + i/(i+1)

Write a test program that displays the following table:

i m(i)

1 0.5000

2 1.1667

...

19 16.4023

20 17.3546
'''

def add(num):
    total = 0
    total = num / (num+1)
    return total

i = 1
total = 0
for i in range(1, 21):
    total += add(i)
    print(i, format(total, ".4f"))
