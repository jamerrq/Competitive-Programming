import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()

for _ in range(t):
    l, r, x = readList()
    a, b    = readList()

    # a, b = max(a, b), min(a, b)

    lf_b = b - x
    rg_b = b + x

    if a == b:
        print(0)
        continue

    if lf_b < l and rg_b > r:
        print(-1)
        continue

    # print(a, b)
    if a > b:
        # print('hell')

        # intento llegar directo
        if a - b >= x:
            print(1)
            continue

        # intento llegar por izquierda
        if lf_b >= l and a - lf_b >= x:
            print(2)
            # print('here 1')
            continue

        # intento llegar por derecha:
        if rg_b <= r and rg_b - a >= x:
            print(2)
            # print('here 2')
            continue

        # intento llegar en 3 pasos
        if a - l >= x and r - l >= x and r - b >= x:
            print(3)
            # print('here 3')
            continue

        if r - a >= x and r - l >= x and b - l >= x:
            print(3)
            # print('here 4')
            continue

        print(-1)

    else:

        # intento llegar directo
        if b - a >= x:
            print(1)
            continue

        # intento llegar por izquierda
        if lf_b >= l and a - lf_b >= x:
            print(2)
            # print('here 1')
            continue

        # intento llegar por derecha:
        if rg_b <= r and rg_b - a >= x:
            print(2)
            # print('here 2')
            continue

        # intento llegar en 3 pasos
        if a - l >= x and r - l >= x and r - b >= x:
            print(3)
            # print('here 3')
            continue

        if r - a >= x and r - l >= x and b - l >= x:
            print(3)
            # print('here 4')
            continue

        print(-1)
