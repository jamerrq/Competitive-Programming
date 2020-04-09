import sys

w = sys.stdin.readline().split()
w = w[0]
a = sys.stdin.readline().split()
a = a[0]

z = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = []
for i in range(len(z)):
    n.append(i)

d = ''

for i in range(len(w)):
    index = z.index(w[i])
    index -= z.index(a[i])
    if index < 0:
        index += 26
    d += z[index]
    a += z[index]

print(d)
