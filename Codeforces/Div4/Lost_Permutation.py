import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
for _ in range(t):
    m, s = readList()
    B = readList()
    mapa = {}
    maxB = max(B)
    suma = 0
    for bi in B:
        mapa[bi] = 1
    for i in range(1, maxB):
        if not mapa.get(i, 0):
            suma += i

    if suma > s:
        print('NO')
    else:
        # print(suma, s)
        s -= suma
        init = maxB
        while s > 0:
            init += 1
            s -= init
            # print(f'suma - {init}')

        if s == 0:
            print('YES')
        else:
            # print('here')
            print('NO')
