import sys

def rl():
    line = sys.stdin.readline()
    return line

line = rl().split()

s, t, n = int(line[0]), int(line[1]), int(line[2])

line = rl().split()

ds = list(map(int, line))

line = rl().split()

bs = list(map(int, line))

line = rl().split()

cs = list(map(int, line))

start = s

for i in range(n):
    start += ds[i]
    start += (cs[i] - start % cs[i]) % cs[i]
    start += bs[i]

start += ds[-1]

if start > t:
    print('no')
else:
    print('yes')
