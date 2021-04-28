#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    last_digit_of = number % 10

else:
    last_digit_of = number % (-10)

if last_digit_of > 5:
    print("Last digit of {} is {:d} and is greater than 5"
          .format(number, last_digit_of))

if last_digit_of == 0:
    print("Last digit of {} is {:d} and is 0".format(number, last_digit_of))

elif last_digit_of < 6 != 0:
    print("Last digit of {} is {:d} and is less than 6 and not 0"
          .format(number, last_digit_of))
