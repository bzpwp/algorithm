from collections import Counter

q = int(input())

d = Counter()

for i in range(q):
    que = input()
    if que[0]=="1":
        y,x = map(int, que.split())
        d[x]+=1
    elif que[0]=="3":
        print(max(d)-min(d))
    else:
        y,x,c = map(int, que.split())
        if d[x]-c > 0:
            d[x]-=c
        else:
            del d[x]