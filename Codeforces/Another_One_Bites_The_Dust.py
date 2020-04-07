import sys
 
line = sys.stdin.readline().split()
a, b, c = int(line[0]), int(line[1]), int(line[2])
 
max_l = c * 2 + 2 * min(a, b)
if a != b and a != 0 and b != 0:
    max_l += 1
 
print(max_l)