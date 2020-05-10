import sys

items = []

for _ in range(int(sys.stdin.readline())):
    si = sys.stdin.readline().split()[0]
    items.append(si)


print(len(set(items)))
