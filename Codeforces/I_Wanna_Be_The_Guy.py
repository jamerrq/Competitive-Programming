import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


n = read()
l1 = readList()
l2 = readList()
s = set()

for i in l1[1:]:
    s.add(i)

for i in l2[1:]:
    s.add(i)


if len(s) == n:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')
