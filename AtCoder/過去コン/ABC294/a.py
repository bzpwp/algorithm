n = int(input())
ls = list(map(int,input().split()))

l = []
for i in ls:
    if i%2==0:
        l.append(i)
print(*l)