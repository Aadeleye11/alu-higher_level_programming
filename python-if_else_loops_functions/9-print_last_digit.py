#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number  # Handle negative numbers
    last_digit = number % 10  # Get the last digit
    print(last_digit, end="")  # Print the last digit
    return last_digit
