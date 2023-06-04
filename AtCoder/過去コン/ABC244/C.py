from sys import stdin
n = int(input())
l = list(range(1,2*n+2))
from collections import deque
import sys
d = set(l)
for i in range(n+1):
    num = int(stdin.readline())
    if num == 0:
        sys.exit()
    else:
        d.remove(num)
        sys.stdout.write(d.pop())
        sys.stdout.flush()