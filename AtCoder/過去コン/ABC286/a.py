n,p,q,r,s = map(int,input().split())
ls = list(map(int,input().split()))

for i in range(q-p+1):
# for i in range(1,2):
    ls[p-1+i], ls[r-1+i] = ls[r-1+i], ls[p-1+i]

print(*ls)