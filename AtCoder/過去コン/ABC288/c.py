n,m = map(int,input().split())

T_list = [list(map(int,input().split())) for _ in range(m)]
# defaultdictでtreeを表現
from collections import defaultdict as ddict
tree = ddict(list)
for t in T_list:
    tree[t[0]].append(t[1])
    tree[t[1]].append(t[0])

A = 0
visited = set([])
from collections import deque
def dfs(T,i,j):
    global A, visited
    # Q = deque([i])
    # q = Q.popleft()
    for c in T[i]:
        if c == j:
            continue
        elif c in visited:
            # print(c,j,A)
            A += 1
        else:
            visited.add(c)
            dfs(T,c,i)

for i in range(n):
    if i+1 not in visited:
        dfs(tree,i+1,0)

print(A//2)