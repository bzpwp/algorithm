n = int(input())
from collections import defaultdict
dd=defaultdict(int)
for i in range(n):
    s = input()
    x = dd[s]
    if x == 0:
        print(s)
        dd[s]=1
    else:
        print(s+"("+str(x)+")")
        dd[s]+=1