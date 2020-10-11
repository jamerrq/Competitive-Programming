import sys


def readInt():
    return int(sys.stdin.readline())

def readList(type=int):
    return list(map(int, sys.stdin.readline().split()))
