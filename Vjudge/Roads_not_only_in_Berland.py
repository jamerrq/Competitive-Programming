import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


class City(object):

    def __init__(self, city_id):
        self.city_id = city_id
        self.next    = None
        self.group   = None


n = read()
cities = [City(i) for i in range(n)]

for _ in range(n - 1):
    ai, bi = readList()
    cities[ai - 1].next = cities[bi - 1]
