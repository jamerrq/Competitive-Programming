import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
for _ in range(t):
    w, h, n = readList()
    maxw = 1
    maxh = 1
    while not w % 2 and w:
        w //= 2
        maxw *= 2
    while not h % 2 and h:
        h //= 2
        maxh *= 2

    #print(maxw, maxh)
    if maxw * maxh >= n:
        print('YES')
    else:
        print('NO')
