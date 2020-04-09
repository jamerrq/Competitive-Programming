import sys

h = sys.stdin.readline().split()
t = 0

d = []

for i in h:
    d.append(i[0])

for i in d:
    t = max(t, d.count(i))

print(t)
