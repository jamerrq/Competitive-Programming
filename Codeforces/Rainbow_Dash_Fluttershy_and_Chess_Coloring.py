import sys


T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    if n % 2:
        print((n + 1) // 2)
    else:
        print((n + 2) // 2)
