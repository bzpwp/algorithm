n, y = map(int, input().split())
total = []
for a in range(n+1): #1万円札がa枚
    for b in range(n+1-a): #5000円札がb枚
        if y == 1000*(n-a-b)+5000*b+10000*a:
            total += [a,b,n-a-b]
if total == []:
    print("-1 -1 -1")
else:
    print("{} {} {}".format(total[0],total[1],total[2]))