#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = len(argv) - 1
    if (n == 0):
        print("0 arguments.")
    else:
        print("{} arguments:".format(n))
        for i in range(n):
            print("{:d}: {:s}".format(i + 1, argv[i + 1]))
