#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
les = "less than 6 and not 0"
ans = "greater than 5" if number % 10 > 5 else "0" if number % 10 == 0 else les
print(f"Last digit of {number:d} is {(number % 10):d} and is " + ans)
