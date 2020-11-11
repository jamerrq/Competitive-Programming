import sys
from typing import Tuple


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


class Item(object):

    def __init__(self, id, Ai, Bi):
        self.id = id
        self.Ai = Ai
        self.Bi = Bi
        self.th = False

    def __repr__(self):
        return '{} {} {}'.format(self.id, self.Ai, self.Bi)


def move(drawers, item, marked):

    if not drawers[item.Ai - 1]:
        drawers[item.Ai - 1] = item
        return True


N, L = readList()
drws = [None] * L
itms = [Item(i, *readList()) for i in range(N)]

for item in itms:
    if not drws[item.Ai - 1]:
        drws[item.Ai - 1] = item
        continue
    if not drws[item.Bi - 1]:
        drws[item.Bi - 1] = item
        continue
    if drws[item.Ai - 1]:
        marked = [False] * N
        curr = item.Ai - 1
        marked[curr] = True
        while drws[item.Ai - 1]:
            pass
