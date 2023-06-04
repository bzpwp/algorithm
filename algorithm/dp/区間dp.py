"""
区間dp
https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1611&lang=jp
"""
n=int(input())
lst=tuple(map(int,input().split()))
#i行j列はjから連続したi個のうち落とせる個数の最大値
dp=[[0]*n for _ in range(n+1)]

#initialize
for j in range(n-1):
    if abs(lst[j]-lst[j+1])<=1 : dp[2][j]=2


#真ん中2*i個が抜けて上下を落とせる場合と2*(i+1)個を複数の部分に分けて落とせる場合の2通りが考えられる
for i in range(3,n+1):
    for j in range(n-i+1):
        mx=0
        if i%2==0:
            if abs(lst[j]-lst[j+i-1])<=1:
                if dp[i-2][j+1]==i-2:
                    dp[i][j]=i
                    continue
            mx=dp[i-2][j+1]                
            for k in range(2,i,2):
                if mx<dp[k][j]+dp[i-k][j+k]:
                    mx=dp[k][j]+dp[i-k][j+k]
                    if mx==i:break
        else :
            for k in range(1,i,2):
                if mx<dp[k][j]+dp[i-k][j+k]:
                    mx=dp[k][j]+dp[i-k][j+k]                
        dp[i][j]=mx
print(dp[n][0])        
#print(dp) 
