import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
for _ in range(t):
    a, b, k = readList()
    boys = readList()
    girls = readList()
    dict1 = {}
    dict2 = {}
    for boy in boys:
        dict1[boy] = dict1.get(boy, 0) + 1
    for girl in girls:
        dict2[girl] = dict2.get(girl, 0) + 1

    ans = 0
    for boy, girl in zip(boys, girls):
        ans += k - dict1[boy] - dict2[girl] + 1

    print(ans // 2)
