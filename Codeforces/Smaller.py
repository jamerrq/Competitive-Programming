from enum import Flag
import sys
from turtle import Turtle


def read(func=int):
    return func(sys.stdin.readline().strip())


def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
for _ in range(t):

    q = read()
    aA, bA = True, True
    aL, bL = 1, 1

    for _ in range(q):

        d, k, x = readList(str)
        xL = len(x) * int(k)

        if d == '1':

            aL += xL
            for char in x:
                if char != 'a':
                    aA = False

        else:
            bL += xL
            for char in x:
                if char != 'a':
                    bA = False

        # print()

        if not bA:
            print('YES')
        else:
            if not aA:
                print('NO')
            else:
                if aL < bL:
                    print('YES')
                else:
                    print('NO')
