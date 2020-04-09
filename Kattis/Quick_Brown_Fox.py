import sys

n = int(sys.stdin.readline())

az = 'abcdefghijklmnopqrstuvwxyz'

for i in range(n):
    line = sys.stdin.readline().lower()
    ms = ''
    for j in az:
        if line.count(j) == 0:
            ms += j
    if len(ms) == 0:
        print('pangram')
    else:
        print('missing {}'.format(ms))
