import sys


class Node(object):

    def __init__(self, id):
        self.id = id
        self.ns = []


class Graph(object):

    def __init__(self, nodes):
        self.nodes = nodes


    def BFS(self, s):

        distances = [-1] * len(self.nodes)
        queue = []
        queue.append(s)
        distances[s] = 0

        while queue:
            s = queue.pop(0)
            for node in self.nodes[s].ns:
                if distances[node] == -1:
                    distances[node] = distances[s] + 6
                    queue.append(node)

        return distances


q = int(sys.stdin.readline())
for _ in range(q):
    n, m = map(int, sys.stdin.readline().split())
    nodes = [None] * n
    for i in range(n):
        nodes[i] = Node(i)

    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        nodes[u - 1].ns.append(v - 1)

    s = int(sys.stdin.readline()) - 1
    graph = Graph(nodes)
    distances = graph.BFS(s)
    print(' '.join([str(x) for x in distances if x != 0]))
