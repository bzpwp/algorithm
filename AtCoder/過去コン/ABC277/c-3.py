n = int(input())
from collections import defaultdict
dd = defaultdict(list)
for i in range(n):
    a,b = map(int,input().split())
    dd[min(a,b)].append(max(a,b))

x = 1
from collections import deque
def dfs(T,i,init=True):
    global x
    # if init==True:
    #     print(i)
    Q = deque([i])
    q = Q.popleft()
    for c in T[q]:
        x = max(x,c)
        dfs(T,c,False)

dfs(dd,1)

print(x)