#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(f"{} is positive")
elif number < 0:
    print(f"{} is negative")
elif number == 0:
    print(f"{} is zero")
else: 
    print("wrong type")
