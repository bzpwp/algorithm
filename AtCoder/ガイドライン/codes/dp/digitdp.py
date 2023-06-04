#https://torus711.hatenablog.com/entry/20150423/1429794075


"""
n以下の整数の数dp[ L ][ 0 ] + dp[ L ][ 1 ] 
n未満の整数の数dp[ L ][ 0 ] 
"""

s = input()
dp = [[0 for _ in range(2)] for __ in range(len(s)+1)]
dp[0][0] = 1
for i in range(len(s)):
    D = int(s[i])
    for j in range(2):
        for d in range(0, 10 if j else D+1):
            dp[i+1][j or (d < D)] += dp[i][j]