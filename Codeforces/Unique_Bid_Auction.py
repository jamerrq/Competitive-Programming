import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
for _ in range(t):
    n = read()
    A = readList()
    B = list(enumerate(A))
    #print(B)
    B.sort(key=lambda x:x[1])
    #print(B)
    found = False
    for i in range(n):
        if i == 0:
            if n == 1 or B[i][1] != B[i + 1][1]:
                print(B[i][0] + 1)
                found = True
                break
        elif i < n - 1:
            if B[i][1] != B[i - 1][1] and B[i][1] != B[i + 1][1]:
                print(B[i][0] + 1)
                found = True
                break
        else:
            if B[i][1] != B[i - 1][1]:
                print(B[i][0] + 1)
                found = True
                break

    if not found:
        print(-1)
