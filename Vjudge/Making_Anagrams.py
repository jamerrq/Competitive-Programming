import sys


a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

ma = {}
mb = {}

for char in a:
    ma[char] = ma.get(char, 0) + 1

for char in b:
    mb[char] = mb.get(char, 0) + 1


ans = 0
for char in 'abcdefghijklmnopqrstuvwxyz':
    ans += abs(ma.get(char, 0) - mb.get(char, 0))


print(ans)
