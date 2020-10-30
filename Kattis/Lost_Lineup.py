import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


n = read()
D = list(enumerate(readList()))
D.sort(key=lambda x:x[1])
ans = [1] + [x[0] + 2 for x in D]
print(*ans)
