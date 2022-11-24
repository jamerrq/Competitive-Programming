import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


def binary_search(x, A):
    i, j = 0, len(A) - 1
    ans = -1
    while i <= j:
        mid = (i + j) // 2
        if A[mid] >= x:
            ans = mid
            j = mid - 1
        else:
            i = mid + 1

    return ans + 1


t = read()
for _ in range(t):
    n, q = readList()
    A = readList()
    A.sort(reverse=True)
    B = [0] * n
    B[0] = A[0]

    for i in range(1, n):
        B[i] = B[i - 1] + A[i]
    
    #print(B)

    for _ in range(q):
        xj = read()
        if xj > B[-1]:
            print(-1)
        else:
            print(binary_search(xj, B))


# lista = [4, 7, 9, 10]
# lista.sort()
# B = [0] * 4
# B[0] = lista[0]

# for i in range(1, 4):
#     B[i] = B[i - 1] + lista[i]

# print(B)
# print(binary_search(20, B))