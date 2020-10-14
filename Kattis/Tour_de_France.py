import sys


for line in sys.stdin:
    if len(line.split()) == 1:
        break
    f, r = map(int, line.split())
    lin1 = sys.stdin.readline()
    lin2 = sys.stdin.readline()
    F, R = list(map(int, lin1.split())), list(map(int, lin2.split()))
    #zero = int(sys.stdin.readline())
    ratios = []

    for n in R:
        for m in F:
            ratios.append(n/m)

    ratios.sort()
    maxi = 0
    for i in range(len(ratios) - 1):
        maxi = max(maxi, ratios[i + 1] / ratios[i])

    print('{0:.2f}'.format(maxi))
