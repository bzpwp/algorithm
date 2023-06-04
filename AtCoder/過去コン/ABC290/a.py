n,m = map(int,input().split())

lsa = list(map(int,input().split()))
lsb = list(map(int,input().split()))

a = 0
for i in lsb:
    a += lsa[i-1]
print(a)