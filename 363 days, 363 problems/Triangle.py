import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))



def triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


def segment(a, b, c):
    return a + b == c or a + c == b or b + c == a


a, b, c, d = readList()

if triangle(a, b, c) or triangle(a, b, d) or triangle(a, c, d) or triangle(b, c, d):
    print('TRIANGLE')

elif segment(a, b, c) or segment(a, b, d) or segment(a, c, d) or segment(b, c, d):
    print('SEGMENT')

else:
    print('IMPOSSIBLE')

