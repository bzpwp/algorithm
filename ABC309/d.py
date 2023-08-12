n1, n2, m = map(int,input().split())
from collections import defaultdict, deque
graph = defaultdict(list)
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)
dist1 = [0 for _ in range(n1)]
dist2 = [0 for _ in range(n1+n2)]
arrived = [0 for _ in range(n1+n2)]
arrived[0] = 1
arrived[-1] = 1

q1 = deque([1])
q2 = deque([n1+n2])
while q1:
    # print(q1)
    p=q1.popleft()
    for i in graph[p]:
        if not arrived[i-1]:
            # print("--")
            q1.append(i)
            arrived[i-1]=1
            dist1[i-1]=dist1[p-1] + 1

while q2:
    p=q2.popleft()
    for i in graph[p]:
        if not arrived[i-1]:
            q2.append(i)
            arrived[i-1]=1
            dist2[i-1]=dist2[p-1] + 1

# print(dist1)

print(max(dist1) + max(dist2) + 1)

