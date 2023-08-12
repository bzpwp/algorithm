d,n = map(int,input().split())
D = [int(input()) for _ in range(d)]
ls = [list(map(int,input().split())) for _ in range(n)]

dp = [[-1 for _ in range(n)] for _ in range(d)]

t = D[0]
# print("t",t)
for i in range(n):
    a,b,c = ls[i]
    if a<=t<=b:
        dp[0][i] = 0
# print(dp[0])

for i in range(d-1):
    # t1 = D[i]
    t = D[i+1]
    for j in range(n):
        a,b,c = ls[j]
        if a<=t<=b:
            for k in range(n):
                if dp[i][k] >= 0:
                    dp[i+1][j] = max(dp[i+1][j], dp[i][k]+abs(ls[k][2]-c))
print(max(dp[-1]))

# for i in dp:
#     print(i)
        