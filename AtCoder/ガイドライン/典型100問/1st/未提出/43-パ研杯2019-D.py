n = int(input())
flag = []
for i in range(5):
    flag.append(input())

dp = [[float("inf")for _ in range(3)] for __ in range(n+1)]

for i in range(3):
    dp[0][i]=0

#RBW
for i in range(n):
    black = 0
    red = 0
    blue = 0
    white = 0
    for j in range(5):
        if flag[j][i] == "#":
            black += 1
        elif flag[j][i] == "R":
            red += 1
        elif flag[j][i] == "B":
            blue += 1
        elif flag[j][i] =="W":
            white += 1
    dp[i+1][0]=min(dp[i][1],dp[i][2])+black+white+blue
    dp[i+1][1]=min(dp[i][2],dp[i][0])+black+white+red
    dp[i+1][2]=min(dp[i][0],dp[i][1])+black+red+blue

print(min(dp[-1]))