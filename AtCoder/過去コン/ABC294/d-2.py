n,q = map(int, input().split())
from collections import deque
called = deque([])
all = deque([i for i in range(1,n+1)])
went = set([])
for i in range(q):
    a,*x = input()
    if a == "1":
        called.append(all.popleft())
    elif a == "2":
        went.add(int(x[1]))
    elif a == "3":
        x = called.popleft()
        while x in went:
            x = called.popleft()
        print(x,"---")
    print("called",called)
    print("all",all)
    print("went",went)