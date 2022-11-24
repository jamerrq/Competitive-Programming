import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


n = read()
for _ in range(n):
    ans = 'R'
    Bcols = {i:0 for i in range(8)}
    read(str)
    # read(str)
    for _ in range(8):
        row = read(str)
        #print(row)
        for i in range(8):
            if row[i] == 'B':
                Bcols[i] += 1
                if Bcols[i] == 8:
                    ans = 'B'

    print(ans)
