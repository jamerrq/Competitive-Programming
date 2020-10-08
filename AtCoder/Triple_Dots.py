import sys

k = int(sys.stdin.readline())
s = sys.stdin.readline().split()[0]

if len(s) > k:
    s = s[:k] + '...'

print(s)
