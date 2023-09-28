n = int(input())

s = 0
T = 0
votes = []
for i in range(n):
    x,y,z = map(int,input().split())
    s += z
    if x < y:
        votes.append([(y-x)//2+1, z])
    else:
        T += z
needs = s//2+1 -T

if needs <= 0:
    print(0)
    exit()

dp = [[float("inf") for _ in range(needs+1)] for _ in range(len(votes)+1)]
dp[0][0] = 0
for i in range(len(votes)):
    a,b = votes[i] #a人鞍替えでb議席獲得
    for j in range(needs+1):
        if dp[i][j] != float("inf"):
            dp[i+1][j] = min(dp[i+1][j], dp[i][j])
            if j+b>= needs:
                dp[i+1][needs] = min(dp[i+1][needs], dp[i][j]+a)
            else:
                dp[i+1][j+b] = min(dp[i+1][j+b], dp[i][j]+a)

print(dp[-1][-1])