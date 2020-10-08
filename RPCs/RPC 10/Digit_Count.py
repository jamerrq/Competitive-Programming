import sys


a, b, d = map(int, sys.stdin.readline().split())
count   = 0

for i in range(a, b + 1):
    count += str(i).count(str(d))

print(count)
