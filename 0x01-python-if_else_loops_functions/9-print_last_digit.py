#!/usr/bin/python3
def print_last_digit(number):
    last_digit = number % 10
    if last_digit == 0 or number == 0:
        return 0
    elif (last_digit < 0) or (last_digit > 0):
        return last_digit
