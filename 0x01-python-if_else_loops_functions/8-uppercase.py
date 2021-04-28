#!/usr/bin/python3
def uppercase(str):
    for i in str:
        j = ord(i)
        if j in range(97, 123):
            j = j - 32
        print("{:c}".format(j), end="")
    print()
