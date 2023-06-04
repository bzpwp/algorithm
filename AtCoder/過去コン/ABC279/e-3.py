n,m = map(int,input().split())
lsa = list(map(int,input().split()))

A = []

x = 0

ls = list(range(1,n+1))
for i in range(m):
    a = lsa[i]
    # x = ls.index(1)
    if a-1 == x:
        x = a
    elif a == x:
        x = a-1
    A.append(ls[x])
    ls[a-1], ls[a] = ls[a], ls[a-1]
    # print(ls)
    

# print(A)
for i in A:
    print(ls.index(i)+1)