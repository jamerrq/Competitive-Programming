import sys

gn1, gn2, gn3, gn4 = map(int, sys.stdin.readline().split())
em1, em2, em3, em4 = map(int, sys.stdin.readline().split())

vegn = (gn1 + gn3 + gn2 + gn4) / 2
veem = (em1 + em3 + em2 + em4) / 2
if vegn > veem:
    print('Gunnar')
elif veem > vegn:
    print('Emma')
else:
    print('Tie')
