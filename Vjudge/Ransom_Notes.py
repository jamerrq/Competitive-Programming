import sys

m, n = map(int, sys.stdin.readline().split())

freqsm = {}
freqsn = {}

magazine = sys.stdin.readline().split()
note = sys.stdin.readline().split()

for word in magazine:
    freqsm[word] = freqsm.get(word, 0) + 1
for word in note:
    freqsn[word] = freqsn.get(word, 0) + 1

yes = True
for word in freqsn.keys():
    if freqsm.get(word, 0) < freqsn[word]:
        yes = False

if yes:
    print('Yes')
else:
    print('No')
