import sys

n = int(sys.stdin.readline())

line = sys.stdin.readline().split()[::-1]

new = []

for j in range(n):
    if new.count(line[j]) == 0:
        new.append(line[j])

print(len(new))
print(' '.join(new[::-1]))
