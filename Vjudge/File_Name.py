import sys

n = int(sys.stdin.readline())

s = sys.stdin.readline().split()[0]

c = 0

for i in range(len(s)):
    for j in range(len(s)):
        if s[j:].startswith('xxx'):
            c += 1
            s = s[:j] + s[j + 1:]

print(c)
