n = int(input())
l = list(map(int, input().split()))
import collections
c = collections.Counter(l)
ls = c.most_common()
for i in range(n):
    if ls[i][1]==3:
        print(ls[i][0])