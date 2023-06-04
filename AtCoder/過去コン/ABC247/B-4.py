n = int(input())
ls = []
for i in range(n):
    ls.append(list(input().split()))

for a in range(n-1):
    for b in range(a+1,n):
        