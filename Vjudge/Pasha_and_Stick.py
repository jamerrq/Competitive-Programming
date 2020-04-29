import sys

n = int(sys.stdin.readline())

if n % 2 != 0:
    print(0)
else:
    print((n - 1) // 4)
