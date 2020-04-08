import sys

line = sys.stdin.readline().split()
r1, c1, r2, c2 = int(line[0]), int(line[1]), int(line[2]), int(line[3])

rook, bishop, king = 0, 0, 0

if r1 != r2 and c1 != c2:
    rook = 2
else:
    rook = 1

if abs(r1 - r2) == abs(c1 - c2):
    bishop = 1
elif abs(r1 - r2) % 2 == abs(c1 - c2) % 2:
    bishop = 2
else:
    bishop = 0

king = max(abs(r1 - r2), abs(c1 - c2))

print(rook, bishop, king)
