import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    c = 3
    k = 1

    while n % c != 0:
        k += 1
        c += 2 ** k

    print(n // c)
