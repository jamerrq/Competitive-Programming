import sys

line = sys.stdin.readline().split()

def bottles(b, n, c):
    if n > b:
        return c
    return bottles(int(b / n) + b % n, n, c + int(b / n))

print(bottles(int(line[0]) + int(line[1]), int(line[2]), 0))
