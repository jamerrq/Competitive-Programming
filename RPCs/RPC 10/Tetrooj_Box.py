import sys


b, r = map(int, sys.stdin.readline().split())
heights = [0] * b

for _ in range(r):
    h, v, c = map(int, sys.stdin.readline().split())
    maxh = max(heights[c - 1: c + h - 1]) + v
    for i in range(c - 1, c + h - 1):
        heights[i] = maxh


print(max(heights))
