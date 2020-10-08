import sys

n = int(sys.stdin.readline()) % 10

if [2, 4, 5, 7, 9].count(n) > 0:
    print('hon')
elif [0, 1, 6, 8].count(n) > 0:
    print('pon')
else:
    print('bon')
