import sys


while True:
    rows, cols, entr = map(int, sys.stdin.readline().split())
    if rows == 0:
        break
    matrix = [None] * rows
    visitd = [None] * rows
    numbrd = [None] * rows
    for i in range(rows):
        row = sys.stdin.readline().strip()
        toA = []
        for col in row:
            toA.append(col)
        matrix[i] = toA
        visitd[i] = [False] * cols
        numbrd[i] = [0] * cols


    i = 0
    j = entr - 1
    steps = 0
    while True:

        if i < 0 or i >= rows or j < 0 or j >= cols:
            print('{} step(s) to exit'.format(steps))
            break

        status = visitd[i][j]
        #print(status)

        if status:
            start = numbrd[i][j]
            print('{} step(s) before a loop of {} step(s)'.format(start - 1, steps - start + 1))
            break
    
        else:
            steps += 1
            numbrd[i][j] = steps
            visitd[i][j] = True
            next = matrix[i][j]
            if next == 'W':
                j -= 1
            elif next == 'N':
                i -= 1
            elif next == 'S':
                i += 1
            else:
                j += 1
