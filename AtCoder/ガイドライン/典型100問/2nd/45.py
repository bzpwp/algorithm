n,m = map(int,input().split())
codebook = [int(input()) for _ in range(m)]
dp = [[float("inf") for _ in range(6)] for _ in range(n+1)]
dp2 = [[0 for _ in range(6)] for _ in range(n+1)]

for i in range(m):
    dp2[0][i] = 128
    dp[0][i] = 