import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


ABCD = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
C, K = read(str), read(str)
answ = ''
for i in range(len(C)):
    if i % 2:
        to_bc = ABCD.index(K[i])
        new_c = ABCD.index(C[i]) + to_bc
        answ += ABCD[new_c % 26]
    else:
        to_fw = ABCD.index(K[i])
        new_c = ABCD.index(C[i]) - to_fw
        answ += ABCD[new_c % 26]


print(answ)
