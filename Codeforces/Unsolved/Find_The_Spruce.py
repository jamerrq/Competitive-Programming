import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
for _ in range(t):
    n, m = readList()
    matrix = [list(read(str)) for _ in range(n)]
    count = 0
    level = 1
    for i in range(n - level + 1):
        for j in range(level - 1, m - level + 1):
            if matrix[i][j] == '*':
                spruce = True
                lv = 0
                for x in range(i, i + level):
                    for y in range(x - lv + 1, x + lv):
                        if matrix[x][y] != '*':
                            spruce = False

                    lv += 1

                if spruce:
                    count += 1


        level += 1

    print(count)
