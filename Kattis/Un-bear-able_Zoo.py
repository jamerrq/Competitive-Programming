import sys

l = 1

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    zoo = [[],[]]
    for i in range(n):
        line = sys.stdin.readline().split()
        if zoo[0].count(line[-1].lower()) == 0:
            zoo[0].append(line[-1].lower())
            zoo[1].append(1)
        else:
            zoo[1][zoo[0].index(line[-1].lower())] += 1
    print('List {}:'.format(l))
    sort = sorted(zoo[0])
    for i in range(len(zoo[0])):
        print('{} | {}'.format(sort[i], zoo[1][zoo[0].index(sort[i])]))
    l += 1
        
