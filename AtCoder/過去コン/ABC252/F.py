n,l = map(int, input().split())
ls = list(map(int, input().split()))

import heapq

if l-sum(ls)!=0:
    ls.append(l-sum(ls))
    N = n+1
    L = ls
else:
    N = n
    L = ls


ans = 0


que = []
for i in range(N):
    heapq.heappush(que, L[i])

while len(que) > 1:
    l1 = heapq.heappop(que)
    l2 = heapq.heappop(que)
    ans += l1 + l2
    heapq.heappush(que, l1 + l2)

print(ans)