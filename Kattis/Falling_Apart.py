import sys

n = int(sys.stdin.readline())

line = sys.stdin.readline().split()

a = 0
b = 0
d = True

i = []
for c in line:
    i.append(int(c))
    
while len(i) > 0:
    m = max(i)
    ind = i.index(m)
    if d:
        a += m
    else:
        b += m
    i.remove(m)
    d = not d

print(str(a) + ' ' + str(b))
