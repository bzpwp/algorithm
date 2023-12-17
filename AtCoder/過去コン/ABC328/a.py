n,x = map(int,input().split())
ls = list(map(int,input().split()))
a = 0
for i in ls:
    if i <= x:
        a += i
print(a)