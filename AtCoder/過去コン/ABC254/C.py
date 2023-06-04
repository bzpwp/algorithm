n,k  = map(int, input().split())
ls = list(map(int, input().split()))
from collections import deque


le = n//k
amari = n%k
new_l = []
for i in range(k):
    l = []
    if i <amari:
        for j in range(le+1):
            l.append(ls[i+j*k])
        l.sort()
        # l = deque(l)
        # for k in range(le+1):
        #     new_l.append(l.popleft())
        new_l.append(l)
    else:
        for j in range(le):
            l.append(ls[i+j*k])
        l.sort()
        # l = deque(l)
        # for k in range(le):
        #     new_l.append(l.popleft())
        new_l.append(l)
# print(new_l)
# x = []
# for b in range(le+1):
#     for c in new_l:
#         if c!=deque([]):
#             x.append(c.popleft())

# print(x)

# for a in range(n-1):
#     if x[k]>x[k+1]:
#         print("No")
#         exit()
y = 0
z = 0
#print(new_l)
for a in range(le+1):
    #print(a)
    for b in new_l:
        #print(z)
        if z == n:
            print("Yes")
            exit()
        elif y >b[a]:
            print("No")
            exit()
        else:
            y = b[a]
        z += 1
