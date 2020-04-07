import sys
 
w = sys.stdin.readline().split()[0]
 
w = ''.join(sorted(w)) + '-'
 
mp = [[i + 1, None] for i in range(70)]
 
fq = [1] * len(w)
 
for i in range(1, len(w)):
    if w[i] == w[i - 1]:
        fq[i] = fq[i - 1] + 1
    else:
        if mp[fq[i - 1] - 1][1] == None:
            mp[fq[i - 1] - 1][1] = ''
        mp[fq[i - 1] - 1][1] += w[i - 1]
 
 
mp = [x for x in mp if x[1] is not None]
 
to_print = ''
for i in range(len(mp)):
    item = mp[-i-1]
    for j in range(len(item[1])):
        to_print += item[1][j] * item[0]
 
print(to_print)
