import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


rhyme = len(readList(str))
n = read(int)
children = [read(str) for _ in range(n)]
team1 = []
team2 = []

team = True
prev = 0

while children:
    index = (rhyme % len(children) - 1 + prev) % len(children)
    child = children.pop(index)
    if team:
        team1.append(child)
    else:
        team2.append(child)

    prev = index

    team = not team

print(len(team1))
for child in team1:
    print(child)

print(len(team2))
for child in team2:
    print(child)
