import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


while True:
    N, b = readList()
    if N:
        B = readList() + [0]
        s = set()
        for i in range(b):
            for j in range(i + 1, b + 1):
                s.add(abs(B[j] - B[i]))

        if len(s) == N + 1:
            print('Y')
        else:
            print('N')
            #print(s)

    else:
        break
