import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


N = read()
M = {}
for _ in range(N):
    si, ci, di = readList(str)
    if M.get(di):

        if M[di][0] < int(ci):
            M[di] = (int(ci), si)

    else:
        M[di] = (int(ci), si)


ans = sorted([x[1] for x in M.values()])
print(len(ans), *ans, sep='\n')
