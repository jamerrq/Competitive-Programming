import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


class Node(object):

    def __init__(self, num):
        self.num = num
        self.nes = []
        self.tag = num
        self.vis = False


    def put_tag(self, tag):
        self.tag = tag
        for node in self.nes:
            if not node.vis:
                node.put_tag(tag)
                print(f'Hey!, {self.num} {tag}')

case = 0
while True:
    n, m = readList()
    nods = [Node(i) for i in range(n)]
    if n + m:
        for _ in range(m):
            i, j = readList()
            i, j = min(i, j), max(i, j)
            nods[i - 1].nes.append(nods[j - 1])
            #nods[j - 1].nes.append(nods[i - 1])

        for i in range(n):
            nods[i].put_tag(i)


        total = set()
        for i in range(n):
            total.add(nods[i].tag)

        print(f'Case {case + 1}: {len(total)}')
        print(*[node.tag for node in nods])

    else:
        break
