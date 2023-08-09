#!/usr/bin/python3
for i in reversed(range(97, 123)):
    print("{}".format(chr(i - (32 if i % 2 == 1 else 0))), end="")
