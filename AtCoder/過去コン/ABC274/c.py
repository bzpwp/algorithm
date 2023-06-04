n = int(input())
ls = list(map(int,input().split()))


from collections import defaultdict as ddict
# from collections import deque
depth = ddict(int)
depth[1]=0
tree =ddict(list)
for i in range(n):
    a = ls[i]
    d = depth[i]
    x = (i+1)*2
    y = (i+1)*2+1
    tree[d+1].append(x)
    tree[d+1].append(y)
    depth[x]=d+1
    depth[y]=d+1


for i in range(1,2*n+2):
    print(depth[i])