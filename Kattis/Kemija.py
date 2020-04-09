import sys

def decode(s):
  ns = ''
  s1 = False
  s2 = False
  for i in range(len(s)):
    if s1 and s2:
      s1 = False
    elif s2:
      s2 = False
    else:
      ns += s[i]
      if 'aeiou'.count(s[i]) != 0:
        s1 = True
        s2 = True
  return ns

line = sys.stdin.readline()
print(decode(line))