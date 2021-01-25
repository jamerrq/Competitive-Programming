import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


N = read()
S = []
for _ in range(N):
    S.append(read(str))


A = sorted(S)
D = A[::-1]
if S == D:
    print('DECREASING')
elif S == A:
    print('INCREASING')
else:
    print('NEITHER')
