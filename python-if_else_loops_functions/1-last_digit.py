#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
final = abs(number) % 10
if final > 5:
    string = "and is greater than 5"
elif final == 0:
    string = "and is 0"
elif final < 6 and final != 0:
    string = "and is less than 6 and is not 0"
print(f"Last digit of {number} is {final} {string}")
