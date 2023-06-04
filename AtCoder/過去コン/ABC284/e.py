n,m = map(int,input().split())
T_list = [list(map(int,input().split())) for _ in range(m)]
from collections import defaultdict as ddict
tree = ddict(list)
for t in T_list:
    tree[t[0]].append(t[1])
    tree[t[1]].append(t[0])
print(tree)

A = 0

from collections import deque
import copy
def dfs(check, q):
    global tree, A
    # Q = deque([i])
    # q = Q.popleft()
    print("q",q,"A",A,"check",check)
    if q not in check:
    #     return
    # else:
        check.add(q)
        A += 1
        for c in tree[q]:
            check = copy.deepcopy(check)
            dfs(check,c)

dfs(set([]),1)

print(min(10**6,A))




