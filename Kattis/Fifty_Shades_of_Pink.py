import sys

n = int(sys.stdin.readline())

c = 0
for _ in range(n):
    s = sys.stdin.readline().split()[0]
    if s.lower().count('pink') > 0 or s.lower().count('rose') > 0:
        c += 1

if c > 0:
    print(c)
else:
    print('I must watch Star Wars with my daughter')
