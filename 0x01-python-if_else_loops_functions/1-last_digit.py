#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
les = "less than 6 and not 0"
mod = number % 10 * (-1 if number < 0 else 1)
ans = "greater than 5" if mod > 5 else "0" if mod == 0 else les
print(f"Last digit of {number:d} is {mod:d} and is " + ans)
