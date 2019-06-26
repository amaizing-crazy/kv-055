#Write a function decToBin() that taces decimal integer and outputs its binary representation.

def decToBin(num):
    i = 0
    a = [0] * 8
    number = int(num)
    while number  > 0:
        a[i] =number % 2
        i = i + 1
        number = number // 2
    for j in a[::-1]:
        print(a)
decToBin(64)
