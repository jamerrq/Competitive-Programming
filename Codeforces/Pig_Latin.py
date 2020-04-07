import sys

t = int(sys.stdin.readline())

for _ in range(t):
    line = sys.stdin.readline().split()
    if len(line[0]) > 1:
        line[0] = line[0][0].lower() + line[0][1].upper() + line[0][2:]
    pigl = ' '.join([x[1:] + x[0] + 'ay' for x in line])
    print(pigl)
