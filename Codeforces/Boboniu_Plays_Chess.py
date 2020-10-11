import sys


n, m, sx, sy = map(int, sys.stdin.readline().split())

rows = [False] * n
cols = [False] * m

actual_row = sx
actual_col = sy

rows[actual_row] = True
count = 0
while count < n:
    next_row = min([i for i in range(n) if not rows[i]]) + 1
    order = []
