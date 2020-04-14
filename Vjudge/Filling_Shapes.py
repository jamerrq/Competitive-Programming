import sys

n = int(sys.stdin.readline())

if n % 2 != 0 or n == 0:
    print(0)
else:
    print(2 ** (n // 2))
