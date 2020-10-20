import sys


class Martian(object):

    def __init__(self, id):
        self.id     = id
        self.next   = None
        self.length = None
        self.visitd = False

    def set_next(self, martian):
        self.next = martian
    
    def set_length(self, length):
        self.length = length


T = int(sys.stdin.readline())

for k in range(T):

    N = int(sys.stdin.readline())

    M = [None] * N

    for i in range(N):
        M[i] = Martian(i)
    
    for _ in range(N):
        u, v = map(int, sys.stdin.readline().split())
        M[u - 1].set_next(M[v - 1])


    maxi = 0
    did = 0
    for i in range(N):
        count = 0
        temp = [False] * N
        indt = i
        while not temp[indt]:
            count += 1
            temp[indt] = True
            indt = M[indt].next.id
        if count > maxi:
            maxi = count
            did = i + 1
    
    print('Case {}: {}'.format(k + 1, did))
