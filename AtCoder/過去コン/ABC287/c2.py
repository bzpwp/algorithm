n, m = map(int,input().split())
T_list = [list(map(int,input().split())) for _ in range(m)]
from collections import defaultdict as ddict
tree = ddict(list)
for t in T_list:
    tree[t[0]].append(t[1])
    tree[t[1]].append(t[0])

start = 10**6
num_s = 0

for i in tree:
    if len(tree[i]) == 1:
        start = i
        num_s += 1
    elif len(tree[i]) > 2:
        print("No")
        exit()

if num_s > 2 or num_s == 1 or num_s == 0:
    print("No")
    exit()

if len(tree)!=n:
    print("No")
    exit()

print("Yes")
