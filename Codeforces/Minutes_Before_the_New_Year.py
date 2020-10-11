import sys


t = int(sys.stdin.readline())

for _ in range(t):
    hh, mm = map(int, sys.stdin.readline().split())
    minutes = 60 - mm
    hours = (24 - hh - 1) * 60
    print(minutes + hours)
