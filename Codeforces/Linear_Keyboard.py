import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
for _ in range(t):
    keyboard = read(str)
    word = read(str)
    positions = {}
    for i in range(26):
        positions[keyboard[i]] = i

    ans = 0
    for i in range(1, len(word)):
        ans += abs(positions[word[i]] - positions[word[i-1]])

    print(ans)
