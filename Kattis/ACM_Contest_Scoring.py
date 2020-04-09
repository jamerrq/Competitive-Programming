import sys

problems = []
times = []
log = []
status = []

while True:
    line = sys.stdin.readline().split()
    if len(line) == 1:
        break
    if problems.count(line[1]) == 0:
        problems.append(line[1])
        if line[2] == 'right':
            times.append(0)
        else:
            times.append(1)
        log.append(line[0])
        status.append(line[2])
    else:
        n = problems.index(line[1])
        if status[n] == 'wrong':
            if line[2] == 'wrong':
                times[n] += 1
            else:
                status[n] = 'right'
                log[n] = line[0]
        else:
            pass

time = 0
count = 0

for i in range(len(problems)):
    if status[i] == 'right':
        count += 1
        time += int(log[i]) + 20 * int(times[i])

print('%d %d' % (count, time))
