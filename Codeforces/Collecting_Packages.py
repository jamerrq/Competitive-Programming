import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    packages = []
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        packages.append([x, y])
    packages.sort(key=lambda x : (x[0] ** 2 + x[1] ** 2) ** 0.5)
    yes = True
    x = 0
    y = 0
    answer = ''
    for i in range(n):
        xi = packages[i][0]
        yi = packages[i][1]
        if xi >= x and yi >= y:
            answer += 'R' * (xi - x)
            answer += 'U' * (yi - y)
            x = xi
            y = yi
        else:
            yes = False

        if not yes:
            answer = 'NO'
            break
    if yes:
        print('YES')
    print(answer)
