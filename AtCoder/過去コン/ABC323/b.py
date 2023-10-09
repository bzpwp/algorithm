n = int(input())

from collections import defaultdict
dd = defaultdict(int)

for i in range(n):
    s = input()
    for j in range(i+1,n):
        if s[j] == "o":
            dd[i+1] += 1
        else:
            dd[j+1] += 1

ls = [[dd[i+1],i+1] for i in range(n)]
ls.sort(reverse=True)
dd2 = defaultdict(list)
for i in range(n):
    dd2[ls[i][0]].append(ls[i][1])
A = []
wins = list(set([ls[i][0] for i in range(n)]))
wins.sort(reverse=True)
for i in wins:
    x = dd2[i]
    x.sort()
    A += x
print(*A)