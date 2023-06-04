n,k = map(int, input().split())
ls = list(map(int,input().split()))
sls = []
for i in range(n):
    sls.append(sum(ls[i:]))
all = []
for a in range(n-1):
    for b in range(a+1,n):
        all.append(sls[a]-sls[b])
all += sls
print(all.count(k))