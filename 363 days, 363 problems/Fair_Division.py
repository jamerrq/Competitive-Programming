import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
for _ in range(t):
    _ = read()
    A = readList()
    twos = A.count(2)
    ones = A.count(1)
    ans = 'NO'
    if sum(A) % 2:
        print(ans)
        continue
    else:
        if twos % 2:
            if ones > 1:
                ans = 'YES'
        else:
            ans = 'YES'

    print(ans)
