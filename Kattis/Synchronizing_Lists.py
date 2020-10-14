import sys


while True:

    n = int(sys.stdin.readline())

    if not n:
        break

    l1 = []
    for _ in range(n):
        l1.append(int(sys.stdin.readline()))
    l2 = l1.copy()
    l3 = []
    for _ in range(n):
        l3.append(int(sys.stdin.readline()))
    l2.sort()
    l3.sort()
    m1 = {}
    for i in range(n):
        m1[l2[i]] = l3[i]
    for i in range(n):
        print(m1[l1[i]])
