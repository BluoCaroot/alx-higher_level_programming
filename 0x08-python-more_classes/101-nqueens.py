#!/usr/bin/python3

from sys import argv

def solve(column, board, ans, y, xy, yx, n):
    if column == n:
        ans.append(board)
        return

    for row in range(0, n):
        if not y[row] and not xy[column + row] and not yx[n - 1 + column - row]:
            y[row] = 1
            xy[column + row] = 1
            yx[n - 1 + column - row] = 1
            x = board + [[column, row]]
            solve(column + 1, x, ans, y, xy, yx, n)
            y[row] = 0
            xy[column + row] = 0
            yx[n - 1 + column - row] = 0


if len(argv) != 2:
    print("Usage: nqueens N")
    exit(1)
n = argv[1]
if not  n.isdigit():
    print("N must be a number")
    exit(1)
n = int(n)
if n < 4:
    print("N must be at least 4")
    exit(1)
ans = []
board = []
y = [0] * n
xy = [0] * ((2 * n) - 1)
yx = [0] * ((2 * n) - 1)
solve(0, board, ans, y, xy, yx, n)

for i in ans:
    print(i)
