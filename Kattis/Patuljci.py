import sys

dwarves = []

for i in range(9):
    dwarve = int(sys.stdin.readline())
    dwarves.append(dwarve)

def patuljci(dwarves, i, s, c, t):
    if i == len(dwarves):
        if s == 100:
            t.append(c)
    else:
        patuljci(dwarves, i + 1, s + dwarves[i], c + "-" + str(dwarves[i]), t)
        patuljci(dwarves, i + 1, s, c, t)

answer = []
patuljci(dwarves, 0, 0, "", answer)
answers = []
for i in range(len(answer)):
    a = answer[i].split("-")
    if len(a) == 8:
        answers.append(a)

for i in range(1,len(answers[0])):
    print answers[0][i]
