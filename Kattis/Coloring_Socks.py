import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


S, C, K = readList()
socks = readList()
socks.sort()

answ = 1
curr = []
for sock in socks:
    if not curr:
        curr = [sock]
        continue
    if len(curr) > 0 and len(curr) < C and abs(curr[0] - sock) <= K:
        curr.append(sock)
    else:
        curr = [sock]
        answ += 1


print(answ)
