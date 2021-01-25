import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


n = read()
q = []
for _ in range(n):
    q.append(read())

print(*q[::-1], sep='\n')
