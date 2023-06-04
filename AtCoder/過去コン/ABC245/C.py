

n,k = map(int, input().split())
lsa = list(map(int, input().split()))
lsb = list(map(int, input().split()))

for i in range(1,n):
    c = abs(lsa[i]-lsa[i-1])
    d = abs(lsb[i]-lsa[i-1])
    e = abs(lsa[i]-lsb[i-1])
    f = abs(lsb[i]-lsb[i-1])
    if 