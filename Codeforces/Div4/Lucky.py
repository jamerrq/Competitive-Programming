import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))



t = read()
for _ in range(t):
    num = read(str)
    if int(num[0]) + int(num[1]) + int(num[2]) == \
        int(num[3]) + int(num[4]) + int(num[5]):
        print('YES')
    else:
        print('NO')
