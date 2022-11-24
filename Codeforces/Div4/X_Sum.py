import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


def get_up_left(i, j, matrix):
    if i and j:
        return matrix[i - 1][j - 1] + get_up_left(i - 1, j - 1, matrix)
    else:
        return 0

def get_up_right(i, j, matrix):
    ncol = len(matrix[0])
    if i and j < ncol - 1:
        return matrix[i - 1][j + 1] + get_up_right(i - 1, j + 1, matrix)
    else:
        return 0

def get_down_left(i, j, matrix):
    nrow = len(matrix)
    if i < nrow - 1 and j:
        return matrix[i + 1][j - 1] + get_down_left(i + 1, j - 1, matrix)
    else:
        return 0

def get_down_right(i, j, matrix):
    nrow = len(matrix)
    ncol = len(matrix[0])
    if i < nrow - 1 and j < ncol - 1:
        return matrix[i + 1][j + 1] + get_down_right(i + 1, j + 1, matrix)
    else:
        return 0

def get_sum_diagonals(i, j, matrix):
    return matrix[i][j] + get_up_left(i, j, matrix) + get_up_right(i, j, matrix) + \
        get_down_left(i, j, matrix) + get_down_right(i, j, matrix)


t = read()
for _ in range(t):
    n, m = readList()
    board = [readList() for _ in range(n)]
    max_cost = get_sum_diagonals(0, 0, board)
    for i in range(n):
        for j in range(m):
            tmp_cost = get_sum_diagonals(i, j, board)
            if tmp_cost > max_cost:
                max_cost = tmp_cost
    
    print(max_cost)
