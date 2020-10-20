import sys


class Adventurer(object):

    def __init__(self, nm, s1, s2, s3):
        self.nm = nm
        self.s1 = int(s1)
        self.s2 = int(s2)
        self.s3 = int(s3)
        self.ch = False

    def __repr__(self):
        return self.nm


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().split()))


n = read()
A = [None] * n
for i in range(n):
    name, s1, s2, s3 = readList(str)
    A[i] = Adventurer(name, s1, s2, s3)

team = []

while len(A) + len(team) > 2:
    A.sort(key=lambda x:x.nm)
    if len(team) == 3:
        team.sort(key=lambda x:x.nm)
        print(*team)
        team.clear()
    if len(team) + len(A) < 3:
        break
    if len(team) == 0:
        A.sort(key=lambda x:x.s1, reverse=True)
    elif len(team) == 1:
        A.sort(key=lambda x:x.s2, reverse=True)
    else:
        A.sort(key=lambda x:x.s3, reverse=True)

    team.append(A.pop(0))
