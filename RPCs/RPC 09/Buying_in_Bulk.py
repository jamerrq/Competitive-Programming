import sys

c, p = map(int, sys.stdin.readline().split())

print(p*c - 2 * (c - 1))
