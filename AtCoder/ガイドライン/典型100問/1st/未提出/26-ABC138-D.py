n, q = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    # graph[b-1].append(a-1) 

# print(graph)


from collections import defaultdict as ddict
ans = ddict(int)
counter = ddict(int)

for _ in range(q):
    p,x = map(int, input().split())
    counter[p-1]+=x

# print(counter)

def dfs(y):
    z = counter[y]
    ans[y]=z
    for i in graph[y]:
        counter[i]+=z
        dfs(i)

dfs(0)

# print(counter)
# print(ans)
A = []
for i in range(n):
    A.append(ans[i])

print(*A)