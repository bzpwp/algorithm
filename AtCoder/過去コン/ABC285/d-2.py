n = int(input())
slist = set([])
tlist = set([])
from collections import defaultdict
dd = defaultdict(str)

for i in range(n):
    s,t = input().split()
    dd[s]=t
    slist.add(s)
    tlist.add(t)

graph = set([])
while slist:
    x = slist.pop()
    graph.add(x)
    while True:
        x = dd[x]
        if x not in slist:
            tlist.remove(x)
            graph = set([])
            break
        if x in graph:
            # print(graph,x)
            print("No")
            exit()
        else:
            graph.add(x)
            tlist.remove(x)
            slist.remove(x)

print()
print("Yes")