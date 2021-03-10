import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


while True:
    H, U, D, F = readList()
    if H:
        ans = 0
        fac = U * F / 100
        clm = False
        cur = 0
        while True:
            ans += 1
            cur += U
            if cur > H:
                clm = True
                break

            cur -= D
            U -= fac
            U = max(0, U)
            if cur < 0:
                break

        if clm:
            print(f'success on day {ans}')
        else:
            print(f'failure on day {ans}')

    else:
        break
