import sys


n, k = map(int, sys.stdin.readline().split())
impt = []
answ = 0

for _ in range(n):
    l, t = map(int, sys.stdin.readline().split())
    if t:
        impt.append(l)
    else:
        answ += l


impt.sort(reverse=True)
#print(answ, impt[:k], impt[k:])
print(answ + sum(impt[:k]) - sum(impt[k:]))
