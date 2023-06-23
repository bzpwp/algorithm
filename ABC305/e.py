n,m,k = map(int,input().split())
from collections import defaultdict

dd = defaultdict(set)
for i in range(m):
    a,b = map(int,input().split())
    dd[a].add(b)
    dd[b].add(a)

# from collections import deque

police = []

def dfs(arrived,p,h):
    global dd, police
    # if init==True:
    #     print(i)
    # Q = deque([p])
    # q = Q.popleft()
    # print(arrived)
    if h >= 0:
        police.append(p)
        arrived.add(p)
        for c in dd[p]:
            if c not in arrived:
                # print(c, h-1)
                dfs(arrived,c,h-1)

for j in range(k):
    p,h = map(int,input().split())
    arrived = set()
    dfs(arrived,p,h)


police = list(set(police))
police.sort()
print(len(police))
print(*police)