import sys

line = sys.stdin.readline()[:-1]
p1 = p2 = p3 = 0

last = line[0]
for c in line[1:]:
    if c != last:
        p1 += 1
    last = 'U'
    if c != 'U':
        p1 += 1

last = line[0]
for c in line[1:]:
    if c != last:
        p2 += 1
    last = 'D'
    if c != 'D':
        p2 += 1
    #print(p2)

last = line[0]
for c in line[1:]:
    if c != last:
        p3 += 1
    last = c

print(p1)
print(p2)
print(p3)
