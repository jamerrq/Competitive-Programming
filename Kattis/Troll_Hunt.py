import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


b, g, k = readList()
count = 0
b -= 1
while b > 0:
    b -= min(b, g // k)
    count += 1

print(count)
