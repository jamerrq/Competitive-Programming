import sys

n = int(sys.stdin.readline())

s = sys.stdin.readline().split()[0]

t = ''

while len(s) > 0:
    a, s = s[0], s[1:]

    if n % 2 != 0:
        t = t + a
    else:
        t = a + t
    
    n = n - 1

print(t)