n,k = map(int,input().split())
ls = list(map(int,input().split()))
ls.sort()
s = 0
for i in range(len(ls)-k,len(ls)):
    s += ls[i]
print(s)