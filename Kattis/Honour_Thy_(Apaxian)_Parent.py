import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


Y, P = readList(str)
add = 'ex'
if Y[-2:] == 'ex':
    add = ''
elif 'aeiou'.count(Y[-1]):
    Y = Y[:-1]

print(Y + add + P)
