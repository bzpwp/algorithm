n = int(input())
ls = list(map(int,input().split()))

all = [i+1 for i in range(n)]

called = set([])

for j in range(1,n+1):
    if j not in called:
        # print("-",j)
        called.add(ls[j-1])
        all[ls[j-1]-1]=0
        # print(all)
    

all.sort()
import bisect
index = bisect.bisect_left(all,1)
print(len(all[index:]))
print(*all[index:])
