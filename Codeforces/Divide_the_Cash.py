import sys
 
line = sys.stdin.readline().split()
n, d = int(line[0]), int(line[1])
 
scos = []
for _ in range(n):
    scos.append(int(sys.stdin.readline()))
 
ppp = d // sum(scos)
 
for i in range(n):
    print(scos[i] * ppp
