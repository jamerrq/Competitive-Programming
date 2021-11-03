import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
for _ in range(t):
    n = read()
    A = readList()

    m = {}
    odds  = 0
    evens = 0
    for num in A:
        m[num] = m.get(num, 0) + 1
        if num % 2:
            odds += 1
        else:
            evens += 1

    if odds % 2 == 0:
        print('YES')

    else:


        A.sort()
        founded = False
        for i in range(1, n):
            if A[i] == A[i - 1] + 1:
                print('YES')
                founded = True
                break

        if not founded:
            print('NO')
