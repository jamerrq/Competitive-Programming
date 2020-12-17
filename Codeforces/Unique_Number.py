import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
for _ in range(t):
    x = read()
    if x > 45:
        print(-1)
    else:
        count = 9
        s = ''
        while x:
            n = min(count, x)
            x -= n
            s += str(n)
            count -= 1

        s = ''.join(sorted(s))
        print(s)
