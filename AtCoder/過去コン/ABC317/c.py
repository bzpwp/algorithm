n,m = map(int,input().split())

roads = [[0 for _ in range(n)] for _ in range(n)]
for i in range(m):
    a,b,c = map(int,input().split())
    roads[a-1][b-1] = max(c,roads[a-1][b-1])
    roads[b-1][a-1] = max(c,roads[b-1][a-1])

A = 0
print(roads)


from collections import deque
def dfs(T,i,visited, dist):
    global A
    visited.add(i)
    if visited != set([k for k in range(n)]):
        A = max(A, dist)
        Q = deque([i])
        q = Q.popleft()
        print(i, dist, visited)
        for j in range(n):
            # print(j, visited)
            if j not in visited:
                c = T[q][j]
                if c!=0:
                    # print(c, visited)
                    dist += c
                    dfs(T,j,visited,dist)
        visited.remove(i)

# for i in range(n):
#     print(i)
#     dfs(roads,i,set([i]), 0)
dfs(roads,3,set([3]), 0)

print(A)

# print(set([k for k in range(n)]))