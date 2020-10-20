import sys

def readList(type=int):
    return list(map(int, sys.stdin.readline().split()))


def is_dominator(i, j, M, visited=None, seti=set()):
    if not visited:
        visited = [False] * len(M)
    if i == j:
        return seti
    for k in range(len(M[i])):
        if M[i][k] and (not visited[k]):
            seti.intersection_update(is_dominator(k, j, M, visited, seti))

    return seti

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    M = [readList() for _ in range(N)]
    print(is_dominator(0, 4, M))

