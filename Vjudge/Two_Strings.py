import sys

p = int(sys.stdin.readline())

for _ in range(p):
    s1 = sys.stdin.readline().split()[0]
    s2 = sys.stdin.readline().split()[0]
    freqs = {}
    for char in s1:
        freqs[char] = freqs.get(char, 0) + 1
    yes = False
    for char in s2:
        if freqs.get(char):
            yes = True
            break
    if yes:
        print('YES')
    else:
        print('NO')
