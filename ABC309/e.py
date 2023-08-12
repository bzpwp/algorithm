n,m = map(int,input().split())
from collections import defaultdict, deque
tree = defaultdict(list)
h = defaultdict(int)
ls = list(map(int,input().split()))
for i in range(n-1):
    tree[ls[i]].append(i+2)
for i in range(m):
    x,y = map(int,input().split())
    h[x] = max(h[x], y+1)
# print(h)
# print(tree)
q = deque([1])
A = 0
while q:
    p = q.popleft()
    if h[p] >= 1:
        A += 1
        # print(p,"--")
    for i in tree[p]:
        q.append(i)
        h[i] = max(h[i], h[p] -1 )
print(A)