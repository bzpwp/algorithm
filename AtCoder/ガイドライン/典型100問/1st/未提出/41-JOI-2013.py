d,n = map(int,input().split())
temp = []
for i in range(d):
    temp.append(int(input()))
cloth = []
for i in range(n):
    cloth.append(list(map(int,input().split())))

dp = [[0 for _ in range(n)]for __ in range(d)]

for i in range(d-1):
    t1 = temp[i]
    t2 = temp[i+1]
    for j in range(n):
        if cloth[j][0]<=t1 and t1<=cloth[j][1]:
            for k in range(n):
                if cloth[k][0]<=t2 and t2<=cloth[k][1]:
                    dp[i+1][k] = max(dp[i+1][k],(dp[i][j]+abs(cloth[j][2]-cloth[k][2])))

print(max(dp[-1]))