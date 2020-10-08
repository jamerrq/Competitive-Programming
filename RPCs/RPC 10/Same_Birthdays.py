import sys


n = int(sys.stdin.readline())
s = set()
for _ in range(n):
    b = sys.stdin.readline().strip()
    s.add(b)

print(len(s))
