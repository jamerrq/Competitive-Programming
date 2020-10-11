import sys

t = int(sys.stdin.readline())

for _ in range(t):
    s = sys.stdin.readline().split()[0]
    s = 'R' + s + 'R'
    prev = 0
    maxi = 0
    acc = 0
    for i in range(len(s)):
        if s[i] == 'R':
            maxi = max(maxi, acc)
            acc = 0
        else:
            acc += 1
    print(maxi + 1)
