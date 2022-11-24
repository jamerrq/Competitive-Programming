import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


def binary_search(arr, x):

    beg = 0
    end = len(arr) - 1

    while beg < end:

        if beg == end - 1:
            if arr[end] > x:
                return beg
            return end

        mid = (beg + end) // 2

        if arr[mid] <= x:
            beg = mid

        else:
            end = mid - 1

    return beg


t = read()

for _ in range(t):

    n, q = readList()
    A = readList()
    K = readList()

    #
    mA = [0] * n
    cA = [0] * n
    mA[0] = A[0]
    cA[0] = A[0]

    for i in range(1, n):
        mA[i] = max(mA[i - 1], A[i])
        cA[i] = A[i] + cA[i - 1]


    idxs = [binary_search(mA, ki) for ki in K]
    answ = [str(cA[idx]) for idx in idxs]
    for i in range(q):
        if K[i] < A[0]:
            answ[i] = '0'

    print(' '.join(answ))
