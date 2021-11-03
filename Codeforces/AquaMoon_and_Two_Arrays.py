import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
for _ in range(t):
    n = read()
    A = readList()
    B = readList()
    to_up = []
    to_dw = []
    for i in range(n):
        diff = A[i] - B[i]
        #print(diff)
        to_up.extend([i + 1] * diff)
        to_dw.extend([i + 1] * -diff)

    #print(to_up, to_dw)
    if sum(A) == sum(B):
        m = len(to_dw)
        print(m)
        for i in range(m):
            print(to_up[i], to_dw[i])

    else:
        print(-1)
