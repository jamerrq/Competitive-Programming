import sys
from sys import flags


t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    answ = 'NO'
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        c, d = map(int, sys.stdin.readline().split())
        if b == c:
            answ = 'YES'

    if m % 2:
        answ = 'NO'

    print(answ)
