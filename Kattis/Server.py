import sys

line = sys.stdin.readline().split()

numTasks = int(line[0])
time = int(line[1])

count = 0
tasks = sys.stdin.readline().split()
usedTime = 0

for i in range(numTasks):
    if int(tasks[i]) + usedTime > time:
        break
    count += 1
    usedTime += int(tasks[i])

print count
