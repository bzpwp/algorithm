n,q = map(int, input().split())

from collections import defaultdict

dd = defaultdict(int)

for i in range(q):
    y, x = map(int,input().split())
    if y==1:
        dd[x]+=1
    elif y==2:
        dd[x]+=2
    else:
        if dd[x]>=2:
            print("Yes")
        else:
            print("No")