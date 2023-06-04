n,m = map(int, input().split())
lsa = list(map(int, input().split()))
lsb = list(map(int, input().split()))


from collections import deque
import sys

da = deque(lsa)
x = 0
for a in lsb:
    if a in da:
        da.remove(a)
        continue
    else:
        print("No")
        sys.exit()
print("Yes")