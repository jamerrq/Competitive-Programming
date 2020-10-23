import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


while True:

    n = read()
    if n == -1:
        break

    matrix = [readList() for _ in range(n)]
    dont = set()
    for i in range(n):
        to_include = True
        for j in range(i+1, n):
            for k in range(j+1, n):
                if matrix[i][j] and matrix[i][k] and matrix[j][k]:
                    dont.add(i)
                    dont.add(j)
                    dont.add(k)

    ans = [i for i in range(n) if not i in dont]
    print(*ans)
