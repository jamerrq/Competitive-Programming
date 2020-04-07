import sys
 
t = int(sys.stdin.readline())
 
for _ in range(t):
  sys.stdin.readline()
  line = sys.stdin.readline().split()
  nums = list(map(int, line))
 
  res = nums[0] % 2
  yes = True
 
  for i in range(1, len(nums)):
    if nums[i] % 2 != res:
      yes = False
      break
  
  if yes:
    print('YES')
  else:
    print('NO')
