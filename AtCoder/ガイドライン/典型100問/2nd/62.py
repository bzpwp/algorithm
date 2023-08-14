def warshall_floyd(d):
    for k in range(10):
        for i in range(10):
            for j in range(10):
                d[i][j]= min(d[i][j],d[i][k]+d[k][j])
    return d

h,w = map(int,input().split())

# n:頂点数　m:辺の数
# n,m = map(int,input().split())


# ①コスト(存在しないときはinf)
d = [list(map(int,input().split())) for i in range(10)]

# output
d = warshall_floyd(d)

from collections import defaultdict
dd = defaultdict(int)

print(h)
for i in range(h):
    l = list(map(int,input().split()))
    for j in l:
        dd[j] += 1

x = 0
for i in dd:
    if i != -1:
        x += d[i][1]*dd[i]
print(x)