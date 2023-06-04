n,l,t = map(int,input().split())
ls = []
for i in range(n):
    ls.append(list(input().split()))

x = 0
p = []
for a in range(n):
    if ls[a][0]==1:
        p.append(ls[a][1]+t)
    else:
        p.append(ls[a][1]-t)