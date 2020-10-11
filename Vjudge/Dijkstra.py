import sys


class Node(object):

    def __init__(self, id):
        self.id        = id
        self.neiAnDist = {}
        self.neighbors = []
        self.distances = []
        self.visited   = False
        self.prev      = None


class Graph(object):

    def __init__(self, nodes):
        self.nodes = nodes

    def dijkstra(self):
        n            = len(self.nodes)
        distances    = [float('inf')] * n
        distances[0] = 0
        #
        curr = 0
        while True:

            node = self.nodes[curr]

            for i in range(len(node.neighbors)):
                neighbor = node.neighbors[i]
                if self.nodes[neighbor].visited:
                    continue

                distance = node.neiAnDist[node.neighbors[i]]
                if distances[neighbor] > distances[curr] + distance:
                    distances[neighbor] = distances[curr] + distance
                    self.nodes[neighbor].prev = self.nodes[curr]

            node.visited = True

            mini = float('inf')
            for i in range(n):
                if not self.nodes[i].visited and distances[i] < mini:
                    mini = distances[i]
                    curr = i

            if mini == float('inf'):
                break

        return distances


n, m  = map(int, sys.stdin.readline().split())
nodes = [Node(i) for i in range(n)]
for _ in range(m):
    a, b, w = map(int, sys.stdin.readline().split())
    nodes[a - 1].neighbors.append(b - 1)
    nodes[b - 1].neighbors.append(a - 1)
    nodes[a - 1].distances.append(w)
    nodes[b - 1].distances.append(w)
    nodes[a - 1].neiAnDist[b - 1] =\
        min(w, nodes[a - 1].neiAnDist.get(b - 1, float('inf')))
    nodes[b - 1].neiAnDist[a - 1] =\
        min(w, nodes[b - 1].neiAnDist.get(a - 1, float('inf')))

graph = Graph(nodes)
distance = graph.dijkstra()[-1]
if distance == float('inf'):
    print(-1)
else:
    curr = nodes[-1]
    answ = []
    while curr:
        answ.append(curr.id)
        curr = curr.prev

    print(' '.join([str(x + 1) for x in answ[::-1]]))
