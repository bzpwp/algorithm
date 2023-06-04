n = int(input())
ls = list(map(int, input().split()))
M = 998244353



dp = [[] for i in range(n)]

def sousa(x):
    return pow(x, M-2, M)*(x+1)


for i in range(n):
    for j in dp[i]:
        
    x = ls[0]
    dp[i].append({x:sousa[x]})
