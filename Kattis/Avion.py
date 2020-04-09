import sys

lines = []

for i in range(5):
    line = sys.stdin.readline()
    if 'FBI' in line:
        lines.append(str(i + 1))

if len(lines) > 0:
    print(' '.join(lines))
else:
    print('HE GOT AWAY!')
