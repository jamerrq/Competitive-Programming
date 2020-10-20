import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().split()))


def get_score(scores, ind=-1):
    score = 0
    j = 0
    for i in range(len(scores)):
        if i != ind:
            score += scores[i] * (4 / 5) ** j
            j += 1
    return score * (1 / 5)


n = read()
scores = []
for _ in range(n):
    scores.append(read())

avgs = []
for i in range(n):
    avgs.append(get_score(scores, ind=i))


print(get_score(scores))
print(sum(avgs) / n)
