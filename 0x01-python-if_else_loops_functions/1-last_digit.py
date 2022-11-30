#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10 or number % -10
if last_digit > 5:
    info = "and is greater than 5"
elif last_digit == 0:
    info = "and is 0"
else:
    last_digit < 6 and not 0
    info = "and is less than 6 and not 0"
print(f"Last digit of {number} is {last_digit} {info}")
