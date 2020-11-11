import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


score = read(str)
A, B  = 0, 0
for i in range(len(score) // 2):
    if score[2 * i] == 'A':
        A += int(score[2 * i + 1])
    else:
        B += int(score[2 * i + 1])


if A > B:
    print('A')
else:
    print('B')
