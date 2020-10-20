import sys


class Domino(object):

    def __init__(self, id):
        self.id = id
        self.pv = None
        self.nx = None
        self.vs = False


class Graph(object):

    def __init__(self, nodes):
        self.nodes = nodes

    def topoSort(self):
        L = []
        S = [node for node in self.nodes if node.pv is None]
        #print(S)

        while S:
            n = S.pop()
            L.append(n)
            m = n.nx
            if m:
                S.append(m)

        #print(L)
        return L

    def DFSaux(self, node):
        node.vs = True
        if node.nx:
            self.DFSaux(node.nx)

    def DFS(self):
        nodes = self.topoSort()
        #print(nodes)
        count = 0
        for node in nodes:
            if not node.vs:
                self.DFSaux(node)
                count += 1

        return count


t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    tils = [Domino(i) for i in range(n)]
    for _ in range(m):
        x, y = map(int, sys.stdin.readline().split())
        tils[x - 1].nx = tils[y - 1]
        tils[y - 1].pv = tils[x - 1]

    graph = Graph(tils)
    print(graph.DFS())
