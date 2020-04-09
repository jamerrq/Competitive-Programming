import sys

n = int(sys.stdin.readline())

for i in range(n):
    r = sys.stdin.readline().split()
    s = []

    while True:
        line = sys.stdin.readline().split()
        if line[1] == 'goes':
            s.append(line[2])
        else:
            break

    f = '' 

    for c in r:
        if s.count(c) == 0:
            f += c + ' '

    f = f.strip()

    print(f)
