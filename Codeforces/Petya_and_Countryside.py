import sys
 
n = int(sys.stdin.readline())
 
gs = list(map(int, sys.stdin.readline().split()))
 
lf = [1] * n
rg = [1] * n
 
for i in range(1, len(gs)):
    if gs[i] >= gs[i - 1]:
        lf[i] = lf[i - 1] + 1
 
for i in range(len(gs)-2, -1, -1):
    if gs[i] >= gs[i+1]:
        rg[i] = rg[i + 1] + 1 
 
print(max([lf[i] + rg[i] for i in range(len(gs))]) - 1)