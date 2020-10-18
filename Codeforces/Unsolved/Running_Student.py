import sys
from math import sqrt


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().split()))


def get_distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


n, vb, vs = readList()
X = readList()
xu, yu = readList()

min_time, min_dis, ans = float('inf'), float('inf'), -1
i = 2

for xi in X[1:]:

    bus_time = get_distance(0, 0, xi, 0) / vb
    std_time = get_distance(xi, 0, xu, yu) / vs

    if bus_time + std_time < min_time:
        min_time = bus_time + std_time
        min_dis = get_distance(xi, 0, xu, yu)
        ans = i

    elif bus_time + std_time < min_time == min_time:
        if get_distance(xi, 0, xu, yu) < min_dis:
            min_time = bus_time + std_time
            min_dis = get_distance(xi, 0, xu, yu)
            ans = i

    i += 1

print(ans)
