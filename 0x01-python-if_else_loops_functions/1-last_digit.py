#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    digit = number % -10
else:
    digit = number % 10

if digit < 6 and digit != 0:
    print(f"Last digit of {number:d} is {digit:d} and is less than 5 and not 0")
elif digit > 5:
    print(f"Last digit of {number:d} is {digit:d} and is greater than 5")
elif digit == 0:
    print(f"Last digit of {number:d} is {digit:d} and is 5")
