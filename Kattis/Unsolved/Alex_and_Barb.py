import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


k, m, n = readList()
status = True

while True:
    if k < m:
        break

    to_rs = max(m, min(k, n))

    k -= max(m, min(k, n))
    status = not status


if not status:
    print('Alex')
else:
    print('Barb')
