import sys

t = int(sys.stdin.readline())

lets = 'abcdefghijklmnopqrstuvwxyz'

for _ in range(t):
    n, a, b = map(int, sys.stdin.readline().split())
    s = ''
    while len(s) < n:
        s += lets[:b]
    s = s[:n]
    print(s)
