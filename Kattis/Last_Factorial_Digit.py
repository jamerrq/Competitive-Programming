import sys

n = int(sys.stdin.readline())

f = ['1', '2', '6', '4']

for i in range(n):
    h = int(sys.stdin.readline())
    if h > 4:
        print(0)
    else:
        print(f[h - 1])
