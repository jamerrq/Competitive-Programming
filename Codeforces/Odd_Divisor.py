import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
for _ in range(t):
    n = read()
    ans = 'NO'
    while n:
        if n % 2 and n > 1:
            ans = 'YES'
            break
        n //= 2

    print(ans)
