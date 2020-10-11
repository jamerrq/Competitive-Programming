import sys


def cut_cost(C, lb, ub):
    if len(C) == 1:
        return ub - lb
        #print(1, ub, lb)
    if len(C) == 2:
        #print(ub, lb, C[0])
        return ub - lb + C[0]

    n = len(C) // 2
    lb1, ub1 = 0, C[n]
    #print(lb1, ub1, C[:n])
    lb2, ub2 = C[n], ub
    #print(lb2, ub2, C[n + 1:])
    return cut_cost(C[:n], lb1, ub1) + cut_cost(C[n + 1:], lb2, ub2)


while True:
    l = int(sys.stdin.readline())
    if l == 0:
        break
    n = int(sys.stdin.readline())
    C = list(map(int, sys.stdin.readline().split()))
    #cut_cost(C, 0, l)
    print(cut_cost(C, 0, l))
