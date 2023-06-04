n,m = map(int,input().split())
ls = []
for i in range(m):
    ls.append(list(map(int,input().split())))
lsp = list(map(int,input().split()))

ans = 0

for i in range(2**n):
    x = 0
    for j in range(m): 
        k = ls[j][0]
        y = 0
        for l in range(k): 
            if i >> ls[j][l+1]-1 & 1:
                y += 1
        if y%2 == lsp[j]:
            # print("--")
            # print(i,j)
            x += 1

    if x == m:
        ans += 1

print(ans)