import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
for _ in range(t):

    n, q = readList()
    A = readList()
    sumPar   = 0
    sumImpar = 0
    sumTotal = 0

    for num in A:
        if num % 2:
            sumImpar += 1
        else:
            sumPar += 1

        sumTotal += num

    for _ in range(q):
        ti, xi = readList()
        if ti:
            sumTotal += xi * sumImpar
            if xi % 2:
                sumPar += sumImpar
                sumImpar = 0
        else:
            sumTotal += xi * sumPar
            if xi % 2:
                sumImpar += sumPar
                sumPar = 0

        print(sumTotal)
