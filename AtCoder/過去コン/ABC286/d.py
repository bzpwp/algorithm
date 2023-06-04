n,K = map(int,input().split())   
a = []
m = []
for i in range(n):
    A, B = map(int,input().split())
    a.append(A)
    m.append(B)

MAX_K = 10**4

dp = [-1] * (MAX_K + 1)    # DPテーブル

dp[0] = 0
for i in range(n):
    for j in range(K + 1):
        if dp[j] >= 0:
            dp[j] = m[i]
        elif j < a[i] or dp[j - a[i]] <= 0:
            dp[j] = -1
        else:
            dp[j] = dp[j - a[i]] - 1
if dp[K] >= 0:
    print("Yes")
else:
    print("No")