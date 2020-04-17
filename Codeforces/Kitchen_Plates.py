import sys

class Char(object):

    def __init__(self, char):
        self.char = char
        self.gret = []
        self.less = []
    
    def add_general(self, sign, char):
        if sign == '>':
            self.add_greater(char)
        else:
            self.add_less(char)

    def add_greater(self, char):
        self.gret.append(char)
        char.less.append(self)
        #self.actualize()

    def add_less(self, char):
        self.less.append(char)
        char.gret.append(self)
        #self.actualize()

    def actualize(self):
        for char in self.gret:
            for g in char.gret:
                if self.gret.count(g) == 0:
                    self.gret.append(g)

        for char in self.less:
            for l in char.less:
                if self.less.count(l) == 0:
                    self.less.append(l)


chars = []
for i in range(5):
    chars.append(Char(chr(i + 65)))

for _ in range(5):
    x, y, z = sys.stdin.readline().split()[0]
    chars[ord(x) - 65].add_general(y, chars[ord(z) - 65])

for char in chars:
    char.actualize()


bugs = False
less = None
mini = 5
for char in chars:
    if len(char.less) < mini:
        mini = len(char.less)
        less = char
    for char2 in chars:
        if char.gret.count(char2) > 0 and char.less.count(char2) > 0:
            bugs = True
            break
    if bugs:
        break

if bugs:
    print('impossible')
else:
    chars.sort(key=lambda x:len(x.gret))
    print(''.join(char.char for char in chars))
