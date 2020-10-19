import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(type=int):
    return list(map(int, sys.stdin.readline().split()))


s = read(str)
x = 0
y = 0

for i in range(len(s)):

    if s[i] == '1':
        x += 2 ** (len(s) - i - 1)
    if s[i] == '2':
        y += 2 ** (len(s) - i - 1)
    if s[i] == '3':
        x += 2 ** (len(s) - i - 1)
        y += 2 ** (len(s) - i - 1)

print(len(s), x, y)
