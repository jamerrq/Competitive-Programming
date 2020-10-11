import sys


t = int(sys.stdin.readline())

for _ in range(t):
    n, s = map(int, sys.stdin.readline().split())
    suma = sum([int(c) for c in str(n)])
    if suma <= s:
        print(0)
    else:
        n1 = int('1' + '0' * len(str(n)))
        print(n1 - n)
