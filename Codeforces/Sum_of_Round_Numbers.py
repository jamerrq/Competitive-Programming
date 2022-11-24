import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


n = read()
for _ in range(n):
    number = read(str)
    aux = []
    idx = 0
    for char in number:
        if char != '0':
            aux.append(char + '0' * (len(number) - idx - 1))

        idx += 1

    if aux:
        print(len(aux))
        print(' '.join(aux))
