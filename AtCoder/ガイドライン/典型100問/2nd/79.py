n,m,q = map(int,input().split())
# trains = [list(map(int,input().split())) for _ in range(m)]
right = [0 for _ in range(n+1)]
mid = [0 for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    right[b] += 1
    if a != b:
        mid[a+1] += 1
        if b+1 < n:
            mid[b+1] -= 1
import itertools
right = list(itertools.accumulate(right))
mid = list(itertools.accumulate(mid))

print(right)
print(mid)

for i in range(q):
    a,b = map(int,input().split())
    print(right[b] - right[a-1] - mid[a])
