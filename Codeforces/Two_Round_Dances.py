import sys
from math import factorial as fact


n = (int(sys.stdin.readline()) + 2)// 2
ans = fact(2 * n + 1) // (n + 1)
print(ans)
