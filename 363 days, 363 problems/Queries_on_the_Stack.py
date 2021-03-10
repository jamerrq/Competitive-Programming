import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


class myInt(object):

    def __init__(self, value):
        self.value = value
        self.maxi = value
        self.mini = value


T = read()
for _ in range(T):
    stack = []
    Q = read()
    for _ in range(Q):
        A = readList()
        if A[0] == 1:
            my_int = myInt(A[1])
            if stack:
                my_int.maxi = max(A[1], stack[-1].maxi)
                my_int.mini = min(A[1], stack[-1].mini)
            stack.append(my_int)
        elif A[0] == 2:
            if stack:
                stack.pop()
        else:
            if stack:
                print(stack[-1].maxi - stack[-1].mini)
            else:
                print('Empty!')
