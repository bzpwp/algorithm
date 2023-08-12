n = int(input())
flag = [input() for _ in range(5)]

dp = [[float("inf") for _ in range(3)] for _ in range(n)]

r = 0
b = 0
w = 0
B = 0
for i in range(5):
    if  flag[i][0] == "R":
        r += 1
    elif flag[i][0] == "B":
        b += 1
    elif flag[i][0] == "W":
        w += 1
    elif flag[i][0] == "#":
        B += 1

dp[0][0] = 5-r
dp[0][1] = 5-b
dp[0][2] = 5-w

for i in range(n-1):
    r = 0
    b = 0
    w = 0
    B = 0
    for j in range(5):
        if  flag[j][i+1] == "R":
            r += 1
        elif flag[j][i+1] == "B":
            b += 1
        elif flag[j][i+1] == "W":
            w += 1
        elif flag[j][i+1] == "#":
            B += 1
    dp[i+1][0] = min(dp[i][1], dp[i][2]) + 5-r
    dp[i+1][1] = min(dp[i][0], dp[i][2]) + 5-b
    dp[i+1][2] = min(dp[i][1], dp[i][0]) + 5-w
print(min(dp[-1]))