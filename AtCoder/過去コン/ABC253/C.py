
from collections import defaultdict

q = int(input())

dd=defaultdict(int)

for i in range(q):
    que = input()
    if que[0]=="1":
        y,x = map(int, que.split())
        dd[x]+=1
    elif que[0]=="3":
        print(max(dd)-min(dd))
    else:
        y,x,c = map(int, que.split())
        dd[x]-=2
    print(dd)