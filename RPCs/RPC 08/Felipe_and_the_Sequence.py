import sys
from math import sqrt


t = int(sys.stdin.readline())

for _ in range(t):
    S = int(sys.stdin.readline())
    n = S ** 2 + 2 * S
    print(n)
