import sys

class Slot(object):

    def __init__(self, w, m, i):
        self.w = w
        self.m = m
        self.i = i

class Coin(object):

    def __init__(self, u, v):
        self.u = u
        self.v = v


s = int(sys.stdin.readline())
slots = []
for i in range(s):
    w, t = map(int, sys.stdin.readline().split())
    slot = Slot(w, t, i + 1)
    slots.append(slot)


c = int(sys.stdin.readline())
coins = []
for _ in range(c):
    u, v = map(int, sys.stdin.readline().split())
    coin = Coin(u, v)
    coins.append(coin)


general_slots = []
dpmatrix = []

maxw = max([slot.w for slot in slots])
maxm = max([coin.v for coin in coins])
maxm = max(maxm, max([slot.m for slot in slots]))

for _ in range(maxw):

    row_slots = [None] * (maxm)
    general_slots.append(row_slots)

    dprow = [float('inf')] * maxm
    dpmatrix.append(dprow)


for slot in slots:

    if general_slots[slot.w - 1][slot.m - 1] is None:
        general_slots[slot.w - 1][slot.m - 1] = slot
        dpmatrix[slot.w - 1][slot.m - 1] = slot.i

    else:
        slott = general_slots[slot.w - 1][slot.m - 1]
        if slott.i > slot.i:
            general_slots[slot.w - 1][slot.m - 1] = slot
            dpmatrix[slot.w - 1][slot.m - 1] = slot.i


for i in range(maxw - 1, -1, -1):

    for j in range(maxm):
        if i == maxw - 1:
            if j != 0:
                dpmatrix[i][j] = min(dpmatrix[i][j], dpmatrix[i][j - 1])

        else:
            if j != 0:
                alt1 = dpmatrix[i + 1][j]
                alt2 = dpmatrix[i][j - 1]
                alt3 = dpmatrix[i][j]
                dpmatrix[i][j] = min([alt1, alt2, alt3])
            else:
                dpmatrix[i][j] = min(dpmatrix[i][j], dpmatrix[i + 1][j])


total = 0
for coin in coins:
    total += dpmatrix[coin.u - 1][coin.v - 1]

print(total)
