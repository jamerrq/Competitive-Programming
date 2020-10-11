import sys

n = int(sys.stdin.readline())

for i in range(n):
    j = n - i - 1
    s = ' ' * j + '#' * (i + 1)
    print(s)
