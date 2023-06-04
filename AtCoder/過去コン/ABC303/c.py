n,m,h,k = map(int,input().split())
s = input()
from collections import defaultdict

# ls = [list(map(int,input().split())) for _ in range(m)]

dd = defaultdict(set)

for i in range(m):
    a,b = map(int,input().split())
    dd[a].add(b)

x = 0
y = 0
p = h
for i in s:
    # print([p,x,y])

    
    if i == "R":
        x += 1
        p -=1
    elif i == "L":
        x -= 1
        p -=1
    elif i == "U":
        y += 1
        p -=1
    elif i == "D":
        y -= 1
        p -=1

    if p < 0:
        print("No")
        exit()
    elif y in dd[x] and p < k:
        p = k
        dd[x].remove(y)
# print(dd)
# print([p,x,y])

print("Yes")