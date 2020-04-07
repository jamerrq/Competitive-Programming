import sys

t = int(sys.stdin.readline())

for _ in range(t):
    line = sys.stdin.readline().split()
    a, b, c, d = int(line[0]), int(line[1]), int(line[2]), int(line[3])
    line = sys.stdin.readline().split()
    x, y, x1 = int(line[0]), int(line[1]), int(line[2])
    y1, x2, y2 =  int(line[3]), int(line[4]), int(line[5])

    lr = b - a
    ud = d - c
    xf = x + lr
    yf = y + ud

    yes = True
    if xf >= x1 and xf <= x2 and yf >= y1 and yf <= y2:
        if a + b > 0:
            if x1 == x == x2:
                yes = False
        if c + d > 0:
            if y1 == y == y2:
                yes = False
    else:
        yes = False

    if yes:
        print('Yes')
    else:
        print('No')
