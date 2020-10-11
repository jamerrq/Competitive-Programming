import sys


n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
q = int(sys.stdin.readline())

twos = {}
fours = {}
eights = {}
sixs = {}

freq = {}


for num in A:
    freq[num] = freq.get(num, 0) + 1
    if freq[num] == 2:
        twos[num] = True
    if freq[num] == 4:
        fours[num] = True
        del twos[num]
    if freq[num] == 6:
        sixs[num] = True
        del fours[num]
    if freq[num] == 8:
        eights[num] = True
        del sixs[num]


for _ in range(q):

    query = sys.stdin.readline().split()
    num = int(query[1])
    if query[0] == '+':
        freq[num] = freq.get(num, 0) + 1
        if freq[num] == 2:
            twos[num] = True
        if freq[num] == 4:
            fours[num] = True
            del twos[num]
        if freq[num] == 6:
            sixs[num] = True
            del fours[num]
        if freq[num] == 8:
            eights[num] = True
            del sixs[num]
    else:
        freq[num] = freq.get(num, 0) - 1
        if freq[num] == 1:
            del twos[num]
        if freq[num] == 3:
            del fours[num]
            twos[num] = True
        if freq[num] == 5:
            del sixs[num]
            fours[num] = True
        if freq[num] == 7:
            del eights[num]
            sixs[num] = True


    ans = 'NO'
    if len(eights) > 0:
        ans = 'YES'
    if len(sixs) > 1:
        ans = 'YES'
    if len(sixs) == 1 and (len(fours) > 0 or len(twos) > 0):
        ans = 'YES'
    if len(fours) > 1:
        ans = 'YES'
    if len(fours) == 1 and (len(twos) > 1):
        ans = 'YES'

    print(ans)
