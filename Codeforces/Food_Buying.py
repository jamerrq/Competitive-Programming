import sys

def function(n):
    if n < 10:
        return n

    add = n // 10

    return n - n % 10 + function(n % 10 + add)

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    print(function(n))
