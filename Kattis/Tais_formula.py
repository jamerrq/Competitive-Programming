import sys

def tai_formula(ts, vs):
  s = 0
  for i in range(len(ts) - 1):
    s += (vs[i] + vs[i + 1]) / 2 * (ts[i + 1] - ts[i])
  return s / 1000

nlines = int(sys.stdin.readline())
ts, vs = [], []

for i in range(nlines):
  line = sys.stdin.readline().split()
  ti   = float(line[0])
  vi   = float(line[1])
  ts.append(ti)
  vs.append(vi)

print(tai_formula(ts, vs))