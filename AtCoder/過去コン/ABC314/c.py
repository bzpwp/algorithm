n,m = map(int,input().split())
s = input()
ls = list(map(int,input().split()))

from collections import defaultdict

dd = defaultdict(list)
dd2 = defaultdict(list)

A = ["" for _ in range(n)]

for i in range(n):
    dd[ls[i]].append(i)
    dd2[ls[i]].append(s[i])
# print(dd)
# print(dd2)

for i in range(m):
    # i+1 color
    points = dd[i+1]
    colors = dd2[i+1]
    # print(colors)
    # print(points)
    for j in range(len(points)):
        A[points[j]] = colors[j-1]
    # print(A)
print("".join(A))