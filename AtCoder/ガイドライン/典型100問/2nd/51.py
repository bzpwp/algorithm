n = int(input())
s = input()

dp = [[0 for _ in range(8)] for _ in range(n)]
f = s[0]
people = {"J":0,"O":1,"I":2}


for i in range(1,8):
    if i>>people[f] & 1:
        if i>>people["J"] & 1:
            dp[0][i] = 1

for i in range(1,n):
    c = s[i]
    for j in range(1,8):
        if j>>people[c] & 1:
            for k in range(1,8):
                if (j & k).bit_count():
                    dp[i][j] += dp[i-1][k]
        dp[i][j] %= 10007

print(sum(dp[-1])%10007)
