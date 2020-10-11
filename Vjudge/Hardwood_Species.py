import sys


t = int(sys.stdin.readline())
sys.stdin.readline()

for i in range(t):
    #sys.stdin.readline()
    mp = {}
    line = 'xsd'
    count = -1
    while line:
        line = sys.stdin.readline().strip()
        mp[line] = mp.get(line, 0) + 1
        count += 1
    keys = list(mp)
    keys.sort()
    keys = keys[1:]
    for key in keys:
        perc = mp[key] / count * 100
        print(key, '{0:.4f}'.format(perc))

    if i != t - 1:
        print()
