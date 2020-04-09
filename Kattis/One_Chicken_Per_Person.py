import sys

line = sys.stdin.readline().split()

n = int(line[0])
m = int(line[1])

if n > m:
    if n != m + 1:
        print('Dr. Chaz needs {} more pieces of chicken!'.format(n - m))
    else:
        print('Dr. Chaz needs {} more piece of chicken!'.format(n - m))
else:
    if m != n + 1:
        print('Dr. Chaz will have {} pieces of chicken left over!'.format(m - n))
    else:
        print('Dr. Chaz will have {} piece of chicken left over!'.format(m - n))
