n,k = map(int,input().split())
ls = [] 
ls = [input() for _ in range(n)]
import collections
import itertools

lsp = []
l = list(range(n))
for i in range(1,n+1):
    lsp.append(list(itertools.combinations(l, i)))

x = 0
for a in lsp:
    for b in a:
        w = ""
        for c in b:
            w += ls[c]
            d = collections.Counter(w)
            x = max(x,list(d.values()).count(k))
print(x)