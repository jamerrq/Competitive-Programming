import sys

n = int(sys.stdin.readline())

for i in range(n):
    line = sys.stdin.readline()
    inline = line.split()
    average = 0
    for j in range(1, len(inline)):
        average += int(inline[j])
    average /= int(inline[0])
    count = 0
    for j in range(1, len(inline)):
        if int(inline[j]) > average:
            count += 1
    percentage = 100 * (count / int(inline[0]))
    print("%.3f%%" % percentage)
    
