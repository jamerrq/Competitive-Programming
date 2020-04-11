import sys

t = int(sys.stdin.readline())

for k in range(t):
    n = int(sys.stdin.readline())
    m = []
    for _ in range(n):
        line = sys.stdin.readline().split()
        nums = list(map(int, line))
        m.append(nums)
    
    trace = 0
    rowsr = 0
    colsr = 0

    for i in range(n):
        one = [False] * n
        two = [False] * n
        for j in range(n):
            if i == j:
                trace += m[i][j]
            if one[m[i][j] - 1]:
                two[m[i][j] - 1] = True
            one[m[i][j] - 1] = True

        rowsr += min(1, sum(two))

    for j in range(n):
        one = [False] * n
        two = [False] * n
        for i in range(n):
            if one[m[i][j] - 1]:
                two[m[i][j] - 1] = True
            one[m[i][j] - 1] = True

        colsr += min(1, sum(two))


    print('Case #{}: {} {} {}'.format(k + 1, trace, rowsr, colsr))
