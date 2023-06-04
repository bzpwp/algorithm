n,q = map(int, input().split())
import bisect
from collections import deque
called = []
went = set([])
all = deque([i for i in range(1,n+1)])
for i in range(q):
    a,*x = input()
    if a == "1":
        called.append(all.popleft())
    elif a == "2":
        ind = bisect.bisect_left(called,int(x[1]))
        called.pop(ind)
    elif a == "3":
        print(called[0])
    # print("called",called)
    # print("all",all)
    