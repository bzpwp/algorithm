n,q = map(int,input().split())
from collections import defaultdict
dd = defaultdict(list)
parent = defaultdict(int)

for i in range(n-1):
    a,b = map(int,input().split())
    dd[a].append(b)
    dd[b].append(a)

def dfs_parent(p,pa):
    parent[p] = pa
    for i in dd[p]:
        if i != pa:
            dfs_parent(i,p)

dfs_parent(1,0)

# print(parent)

c = defaultdict(int)

def dfs(p,x):
    c[p] += x
    for i in dd[p]:
        if i != parent[p]:
            dfs(i,x)


for i in range(q):
    p,x = map(int,input().split())
    dfs(p,x)

A = [c[j] for j in range(1,n+1)]
print(*A)