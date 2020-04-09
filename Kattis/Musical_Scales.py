import sys

n = int(sys.stdin.readline())

line = sys.stdin.readline().split()

notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

scales = [[], [], [], [], [], [], [], [], [], [], [], []]

for i in range(12):
    scale = [notes[i]]
    index = i
    for j in range(7):
        if j != 2 and j != 6:
            index += 2
        else:
            index += 1
        if index >= len(notes):
            index -= len(notes)
        scale.append(notes[index])
    scales[i] = scale

ss = []

for scale in scales:
    b = True
    for n in line:
        if scale.count(n) == 0:
            b = False
            break
    if b:
        ss.append(scale[0])

if len(ss) == 0:
    print('none')
else:
    print(*ss)
