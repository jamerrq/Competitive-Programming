import sys


class Node(object):

    def __init__(self, id):
        self.id = id
        self.pt = None


K = int(sys.stdin.readline())
nodes = [None] * 101

while True:
    lista = list(map(int, sys.stdin.readline().split()))
    #print(lista)
    if len(lista) == 1:
        break
    if nodes[lista[0] - 1] is None:
        nodes[lista[0] - 1] = Node(lista[0])
    for i in range(len(lista) - 1):
        if nodes[lista[i + 1] - 1] is None:
            nodes[lista[i + 1] - 1] = Node(lista[i + 1])
        nodes[lista[i + 1] - 1].pt = nodes[lista[0] - 1]


curr = nodes[K - 1]
ans = []
while curr:
    ans.append(curr.id)
    curr = curr.pt

print(' '.join([str(x) for x in ans]))
