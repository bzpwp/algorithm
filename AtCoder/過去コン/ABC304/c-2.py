n,d = map(int,input().split())
from collections import defaultdict

p = defaultdict(int)
co = defaultdict(set)
p2 = defaultdict(list)


for i in range(n):
    x,y = map(int,input().split())
    p[(x,y)] = i
    co[x].add(y)
    p2[i] = [x,y]

def dfs(n):
    