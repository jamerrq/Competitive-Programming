import sys


class Node(object):

    def __init__(self, id, gain):
        self.id = id
        self.gn = gain
        self.mv = None


    def add_conection(self, node):
        if self.mv is None:
            self.mv = node
        else:
            if node.gn > self.mv.gn:
                self.mv = node


t = int(sys.stdin.readline())

for k in range(t):
    sys.stdin.readline()
    n, m = map(int, sys.stdin.readline().split())
    gain = list(map(int, sys.stdin.readline().split()))
    nods = [None] * n
    for i in range(n):
        nods[i] = Node(i, gain[i])
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        nods[a].add_conection(nods[b])
    
    total_gain = 0
    root = nods[0]
    prev = 0
    while root is not None:
        total_gain += root.gn
        prev = root.id
        root = root.mv

    print('Case {}: {} {}'.format(k + 1, total_gain, prev))
