import sys


n = int(sys.stdin.readline())
x = 0
for _ in range(n):
    op = sys.stdin.readline().strip()
    if op[1] == '+':
        x += 1
    else:
        x -= 1


print(x)
