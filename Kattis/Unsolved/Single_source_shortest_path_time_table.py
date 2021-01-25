import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


class Node(object):

    def __init__(self, id):
        self.id = id
        self.ns = set()
        self.vs = {}

    def add_node(self, node_id, t0, P, d):
        self.ns.add(node_id)
        self.vs[node_id] = [t0, P, d]


while True:
    n, m, q, s = readList()
    if n + m + q + s:
        nodes = [Node(i) for i in range(n)]
        for i in range(m):
            u, v, t0, P, d = readList()
    else:
        break
