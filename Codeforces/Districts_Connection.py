import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
for _ in range(t):
    n = read()
    A = readList()
    #
    d = set()
    m = {}
    k = []
    for i in range(n):
        num = A[i]
        if not num in d:
            d.add(num)
            k.append(num)
        m[num] = m.get(num, []) + [i + 1]

    if len(d) == 1:
        print('NO')
    else:
        print('YES')
        for i in range(len(d)):
            neig = k[i]
            elem = m[k[i]]
            #print(i, k[i], elem)
            if i == 0:
                for j in range(1, len(elem)):
                    print(elem[j], m[k[-1]][0])
            elif i == 1:
                to = i + 1
                if len(d) == 2:
                    to = i - 1
                for j in range(len(elem)):
                    print(elem[j], m[k[to]][0])
            else:
                for j in range(len(elem)):
                    print(elem[j], m[k[0]][0])
