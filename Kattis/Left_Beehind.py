import sys

x = y = -1
while True:
    line = sys.stdin.readline().split()
    x, y = int(line[0]), int(line[1])
    if x == 0 and y == 0:
        break
    if x + y == 13:
        print('Never speak again.')
    elif x > y:
        print('To the convention.')
    elif y > x:
        print('Left beehind.')
    else:
        print('Undecided.')
