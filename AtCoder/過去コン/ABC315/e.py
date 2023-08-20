n = int(input())

from collections import defaultdict

dd = defaultdict(set)
parent = defaultdict(set)
A = set()

for i in range(n):
    c, *p = map(int,input().split())
    dd[i+1] = set(p)

# print(dd)

from collections import deque
def bfs(T,i):
    global parent, A
    Q = deque([i])
    # print(i)
    while Q:
        q = Q.popleft()
        for c in T[q]:
            if c in A:
                dd[parent[c]].remove(c)
                parent[c] = q
            # print(c)
            else:
                parent[c] = q
                A.add(c)
            Q.append(c)
# 1から探索
bfs(dd,1)

Ans = []

def bfs2(T,i):
    global Ans
    Q = deque([i])
    # print(i)
    while Q:
        q = Q.popleft()
        for c in T[q]:
            Ans.append(c)
            Q.append(c)
# 1から探索
bfs2(dd,1)
print(*Ans[::-1])