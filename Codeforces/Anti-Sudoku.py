import sys

t = int(sys.stdin.readline())

mods = [0, 3, 6, 1, 4, 7, 2, 5, 8]

for _ in range(t):
    for i in range(9):
        row = sys.stdin.readline().split()[0]
        mod = mods[i]
        if row[mod] != '2':
            row = row[:mod] + '2' + row[mod + 1:]
        else:
            row = row[:mod] + '1' + row[mod + 1:]
        print(row)
