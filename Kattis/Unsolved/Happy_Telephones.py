import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


class Call(object):

    def __init__(self, id, dest, start, duration):
        self.id = id
        self.dest = dest
        self.start = start
        self.duration = duration


while True:
    N, M = readList();
    if M + N:
        calls = [None] * N
        for i in range(N):
            calls[i] = Call(*readList())

        for _ in range(M):
            start, duration = readList()
            count = N
            for i in range(N):
                call_i = calls[i]
                if call_i.start + call_i.duration < start or call_i.start > start + duration:
                    count -= 1

            print(count)

    else:
        break
