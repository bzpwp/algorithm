n,d = map(int,input().split())
from collections import defaultdict

dd = defaultdict(set)

for i in range(n):
    s = list(input())
    for j in range(d):
        if s[j] == "o":
            dd[i].add(j)

# print(dd)
X = set([i for i in range(d)])
for i in range(n):
    X = X & dd[i]
    # print(i,X)
# X = list(X)
# X.sort()
if len(X) == 0:
    print(0)
    exit()
a = 1
A = 1
for i in range(d-1):
    if i in X and i+1 in X:
        A += 1
        a = max(a,A)        
    else:
        A = 1
print(a)