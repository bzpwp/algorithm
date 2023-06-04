n = int(input())
T_list = []
for i in range(n):
    id, *info = input().split()
    id = int(id)
    for j in range(int(info[0])):
        T_list.append([id,int(info[j+1])])

from collections import defaultdict as ddict
tree = ddict(list)
for t in T_list:
    tree[t[0]].append(t[1])

ans = ddict(list)
ts = 0
went = []
def dfs(i):
    global ts
    went.append(i)
    ts += 1
    ans[i].append(ts)
    for j in tree[i]:
        if j not in went:
            dfs(j)
    ts += 1
    ans[i].append(ts)

dfs(1)

print(ans)

for i in range(n):
    ls = ans[i+1]
    x = ls[0]
    y = ls[1]
    print(i+1,x,y,ls)