# Contest: https://vjudge.net/contest/401919#overview
import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().split()))


name = read(str)
n = read()
priority = {}

actions_value = {
    'posted' : 15,
    'commented' : 10,
    'likes' : 5
}

for _ in range(n):
    action = readList(str)

    name1 = action[0]
    name2 = action[-2][:-2]

    if name1 == name:
        #print(action[1])
        priority[name2] = priority.get(name2, 0) + actions_value[action[1]]
    elif name2 == name:
        priority[name1] = priority.get(name1, 0) + actions_value[action[1]]
    else:
        priority[name1] = priority.get(name1, 0) + 0
        priority[name2] = priority.get(name2, 0) + 0


names = list(priority)
names.sort()
names.sort(key=lambda x:priority.get(x, 0), reverse=True)
for name in names:
    print(name)
