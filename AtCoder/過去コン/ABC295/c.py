n = int(input())
ls = list(map(int,input().split()))

from collections import Counter
c = Counter(ls)
# print(c)
a = 0

for i in c:
    a += c[i]//2
print(a)