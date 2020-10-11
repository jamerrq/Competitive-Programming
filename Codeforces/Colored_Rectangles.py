import sys


class Sticks(object):

    def __init__(self, l):
        self.l = l
        self.m = max(self.l)
    
    def get_stick(self):
        if len(self.l) == 0:
            return 0
        m = self.l.pop()
        if len(self.l) == 0:
            self.m = 0
        else:
            self.m = self.l[-1]
        return m


r, g, b = map(int, sys.stdin.readline().split())

R = list(map(int, sys.stdin.readline().split()))
G = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

R.sort()
G.sort()
B.sort()

SR = Sticks(R)
SG = Sticks(G)
SB = Sticks(B)

ans = 0

while len(SR.l) + len(SG.l) > 0 and len(SG.l) + len(SB.l) > 0:

    if SR.m >= SG.m and SR.m >= SB.m:

        if SG.m >= SB.m:
            ans += SR.get_stick() * SG.get_stick()
        else:
            ans += SR.get_stick() * SB.get_stick()
    
    elif SG.m >= SR.m and SG.m >= SB.m:

        if SR.m >= SB.m:
            ans += SG.get_stick() * SR.get_stick()
        else:
            ans += SG.get_stick() * SB.get_stick()
    
    else:

        if SR.m >= SG.m:
            ans += SB.get_stick() * SR.get_stick()
        else:
            ans += SB.get_stick() * SG.get_stick()

print(ans)
