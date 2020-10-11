import sys

sys.setrecursionlimit(5000)

class Country(object):

    def __init__(self, id):
        self.id = id
        self.ts = []
    

    def __repr__(self):
        return 'Country {}, Astronauts: {}'.format(self.id, self.ts)


class Astronaut(object):

    def __init__(self, id):
        self.id = id
        self.ct = None
        self.pr = []


    def assign_country(self, ct):
        self.ct = ct
        ct.ts.append(self)
        for partner in self.pr:
            if partner.ct is None:
                partner.assign_country(ct)


    def __repr__(self):
        #return 'Id: {}, Partners: {}'.format(self.id, self.pr)
        return 'Id: {}'.format(self.id)


n, p = map(int, sys.stdin.readline().split())
asts = [None] * n

for i in range(n):
    asts[i] = Astronaut(i)

for i in range(p):
    a, b = map(int, sys.stdin.readline().split())
    asts[a].pr.append(asts[b])
    asts[b].pr.append(asts[a])


countries = []
curr = 0
for i in range(n):
    if asts[i].ct is None:
        curr += 1
        country = Country(curr)
        asts[i].assign_country(country)
        countries.append(country)


pops = [len(country.ts) for country in countries]
curr = 0
answ = 0
for i in range(len(pops)):
    curr += pops[i]
    answ += pops[i] * (n - curr)


print(answ)
