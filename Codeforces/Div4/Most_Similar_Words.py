import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))



def get_distance(a, b):
    ia, ib = ord(a), ord(b)
    return abs(ib - ia)


def get_cost(x, y, m):
    return sum([get_distance(x[i], y[i]) for i in range(m)])


t = read()
for _ in range(t):
    n, m = readList()
    words = [read(str) for _ in range(n)]
    min_cost = get_cost(words[0], words[1], m)
    for i in range(n):
        for j in range(i):
            tmp_cost = get_cost(words[i], words[j], m)
            if tmp_cost < min_cost:
                min_cost = tmp_cost
    
    print(min_cost)
