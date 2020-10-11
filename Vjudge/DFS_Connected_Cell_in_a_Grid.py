import sys


def count_cells(matrix, i, j):

    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
        return 0

    if not matrix[i][j]:
        return 0

    matrix[i][j] = 0

    nt = count_cells(matrix, i - 1, j)
    st = count_cells(matrix, i + 1, j)
    ea = count_cells(matrix, i, j + 1)
    we = count_cells(matrix, i, j - 1)
    ne = count_cells(matrix, i - 1, j + 1)
    nw = count_cells(matrix, i - 1, j - 1)
    se = count_cells(matrix, i + 1, j + 1)
    sw = count_cells(matrix, i + 1, j - 1)

    return 1 + nt + st + ea + we + ne + nw + se + sw


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

matrix = [None] * n
for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    matrix[i] = row


maxi = 0
for i in range(n):
    for j in range(m):
        maxi = max(maxi, count_cells(matrix, i, j))


print(maxi)
