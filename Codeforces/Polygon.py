import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    matrix = []
    for _ in range(n):
        matrix.append(sys.stdin.readline().split()[0])
    
    yes = [[True] * n] * n
    for i in range(n):
        maxi = matrix[i][-1]
        for j in range(-2, -n-1, -1):
            if matrix[i][j] > maxi:
                yes[i][j] = False
            maxi = max(matrix[i][j], maxi)

    for j in range(n):
        maxi = matrix[-1][j]
        for i in range(-2, -n-1, -1):
            print(i)
            if matrix[i][j] > maxi:
                yes[i][j] = False or yes[i][j]
            maxi = max(maxi, matrix[i][j])
    
    Yes = True
    for row in yes:
        for col in row:
            if not col:
                Yes = False
                break
        if not Yes:
            break
    if Yes:
        print('YES')
    else:
        print('NO')
