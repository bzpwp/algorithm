n,m = map(int,input().split())
lsa = list(map(int,input().split()))

A = list(range(1,n+1))
for i in lsa:
    A[i-1], A[i] = A[i], A[i-1]

to = [0 for _ in range(n)]
for i in range(n):
    to[A[i]-1] = i+1

# print(to)

ls = list(range(1,n+1))

x = 0
for i in range(m):
    a = lsa[i]
    ls[a-1], ls[a] = ls[a], ls[a-1]
    print(to[ls[x]-1])
    if a-1 == x:
        x = a
    elif a == x:
        x = a-1
    
    # print(x)
    # print(to[ls[x]-1]+1)