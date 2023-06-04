n,s= map(int, input().split())
dp=[[""]*(10000+1) for i in range(n+1)]
# dp=[[""]*(18+1) for i in range(n+1)]
a,b = map(int,input().split())
dp[1][a]="H"
dp[1][b]="T"

ls = []
for i in range(n-1):
    # ls.append(list(input().split()))
    a,b = map(int,input().split())
    for j in range(10000+1):
    # for j in range(18+1):
        if dp[i+1][j]!="":
            dp[i+2][j+a]=dp[i+1][j]
            dp[i+2][j+a] += "H"
            dp[i+2][j+b]=dp[i+1][j]
            dp[i+2][j+b] += "T"

# print(dp)

for k in range(n+1):
    if dp[k][s]!="":
        print("Yes")
        print(dp[k][s])
        exit()

print("No")