N, M = map(int,input().split())
T_list = [list(map(int,input().split()) for _ in range(M))]
from collections import defaultdict as ddict
tree = ddict(list)
for t in T_list:
    tree[t[0]].append(t[1])
    
print(tree)