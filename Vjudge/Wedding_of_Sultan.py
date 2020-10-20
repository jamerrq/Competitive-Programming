import sys

T = int(sys.stdin.readline())


class Sprinkle(object):

    def __init__(self, id):
        self.pr = None
        self.id = id
        self.ps = []

    def set_path(self, spk):
        self.ps.append(spk)

    def set_prev(self, pv):
        self.pr = pv

    def __repr__(self):
        return str(self.id)
    
    def get_paths(self):
        return len(self.ps) + int(self.pr is not None)


for k in range(T):
    s = sys.stdin.readline().strip()
    m = {}

    root = None

    for char in s:
        if not (m.get(char, False)):
            spk = Sprinkle(char)
            if root is None:
                root = spk
            else:
                root.set_path(spk)
                spk.set_prev(root)

            root = spk
            m[char] = spk

        else:
            root = root.pr

    print('Case', k + 1)
    for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if m.get(char, False):
            #print(char, m[char].ps)
            print('{} = {}'.format(char, m[char].get_paths()))
