import sys

t = int(sys.stdin.readline())

for _ in range(t):
    a, b = list(map(int,sys.stdin.readline().split()))
    opt = (a + b) ** 2
    if (a + a) ** 2 >= 2 * (a * b):
        if (a + a) ** 2 < opt:
            opt = (a + a) ** 2
    if (b + b) ** 2 >= 2 * (a * b):
        if (b + b) ** 2 < opt:
            opt = (b + b) ** 2
    if a ** 2 > 2 * (a * b):
        if a ** 2 < opt:
            opt = a ** 2
    if b ** 2 > 2 * (a * b):
        if b ** 2 < opt:
            opt = b ** 2
    print(opt)
