#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ans = f"Last digit of {number:d}"
mod = abs(number) % 10 * -1 if number < 0 else 1
ans += f" is {mod:d} and is "
les = "less than 6 and not 0"
ans += "0" if mod == 0 else "greater than 5" if mod > 5 else les
print(ans)
