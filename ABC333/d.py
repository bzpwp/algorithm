n = int(input())

# defaultdictでtreeを表現
from collections import defaultdict as ddict
import sys
sys.setrecursionlimit(10 ** 10)
tree = ddict(list)
for i in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
    
print(tree) 
x = 10**10
d = 1
from collections import deque
def dfs(T,d,i):
    Q = deque([i])
    q = Q.popleft()
    for c in T[q]:
        print(c)
        dfs(T,c,False)

dfs(tree,0,1)
