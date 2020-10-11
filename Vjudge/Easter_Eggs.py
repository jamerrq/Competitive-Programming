import sys

n = int(sys.stdin.readline())

colors = 'ROYGBIV'

circle = colors[:4] * (n // 4)

m = n - len(circle)
circle += colors[4:]
circle = circle[3-m:]
print(circle)