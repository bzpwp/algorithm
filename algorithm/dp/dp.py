"""
ナップザック(各種1つ)
"""
n,W = map(int,input().split())
dp = [[-1 for _ in range(W+1)] for __ in range(n+1)]
dp[0][0]=0
for i in range(1,n+1):
    v,w = map(int,input().split())
    for j in range(W+1):
        if j-w>=0:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-w]+v)
        else:
            dp[i][j]=dp[i-1][j]
ans = 0
for i in range(W+1):
    ans = max(dp[n][i],ans)
print(ans)

"""
ナップザック(各種1つ)
逆制約
・価値に対する最小の重さ
・dp[i+1][j]:=i番目までの品物から価値の総和がjとなるように選んだときの、重さの総和の最小値(そのような解
が存在しない場合は十分大きな値INF)
"""
n = int(input())
#V = 価値の最大値の総和
W = int(input())
dp = [[float('inf') for _ in range(V+1)] for __ in range(n+1)]
dp[0][0] = 0

A = 0
for i in range(n):
    v,w = map(int,input().split())
    for j in range(V+1):
        if dp[i][j]!=float('inf'):
            dp[i+1][j]=min(dp[i+1][j], dp[i][j])
            if dp[i+1][j]<=W:
                A = max(A,dp[i+1][j])
            dp[i+1][j+v]=min(dp[i+1][j+v], dp[i][j]+w)
            if dp[i+1][j+v]<=W:
                A = max(A,dp[i+1][j+v])
print(A)
 



"""
ナップザック(各種無限個)
"""
n,W = map(int,input().split())
dp = [[-1 for _ in range(W+1)] for __ in range(n+1)]
dp[0][0]=0
for i in range(1,n+1):
    v,w = map(int,input().split())
    for j in range(W+1):
        if j-w>=0:
            dp[i][j]=max(dp[i-1][j],dp[i][j-w]+v)
        else:
            dp[i][j]=dp[i-1][j]
ans = 0
for i in range(W+1):
    ans = max(dp[n][i],ans)
print(ans)

"""
コイン問題(各種無限個)
各値段に要する最小のコイン枚数
"""
n,m = map(int,input().split())
ls = list(map(int,input().split()))

dp = [[float("inf") for _ in range(n+1)] for __ in range(m+1)]
dp[0][0]=0

for i in range(m):
    c = ls[i]
    for j in range(n+1):
        if j-c>=0:
            dp[i+1][j] = min(dp[i][j],dp[i+1][j-c]+1)
        else:
            dp[i+1][j] = dp[i][j]

ans = float("inf")
for i in range(m+1):
    ans = min(ans,dp[i][n])

print(ans)


"""
部分和問題
n個の整数、Aになるか(各種1個)
"""
n, A = map(int,input().split())
ls = list(map(int,input().split()))

#Aは適宜最大値に変える
dp = [[False for _ in range(A+1)] for __ in range(n+1)]

dp[0][0] = True

for i in range(n):
    x = ls[i]
    for j in range(A+1):
        dp[i+1][j] = dp[i][j] or dp[i][max(0,j-x)]

print(dp[-1][A])


"""
部分和問題
n個の整数、Aになるか(各種無限個)
"""
n, A = map(int,input().split())
ls = list(map(int,input().split()))

#Aは適宜最大値に変える
dp = [[False for _ in range(A+1)] for __ in range(n+1)]

dp[0][0] = True

for i in range(n):
    x = ls[i]
    for j in range(A+1):
        dp[i+1][j] = dp[i][j] or dp[i+1][max(0,j-x)]

print(dp[-1][A])

"""
部分和問題
n個の整数、Aになるか(各種有限個)
"""
n, A = map(int,input().split())
#xがy個
ls = [list(map(int,input().split())) for _ in range(n)]

#Aは適宜最大値に変える
dp = [[-1 for _ in range(A+1)] for __ in range(n+1)]
dp[0][0] = 0

for i in range(n):
    dp[i+1][0] = ls[i][1]

for i in range(n):
    x = ls[i][0]
    for j in range(A+1):
        if dp[i][j]>=0:
            dp[i+1][j] = x
        elif j - x < 0:
            dp[i+1][j] = -1
        else:
            dp[i+1][j] = dp[i+1][j-x]-1

if dp[-1][A] >= 0:
    print("Yes")
else:
    print("No")



"""
部分和問題
n個の整数、Aになる組み合わせ数(各種1個)
"""
n, A = map(int,input().split())
ls = list(map(int,input().split()))
M = 1000000009

#Aは適宜最大値に変える
dp = [[0 for _ in range(A+1)] for __ in range(n+1)]
dp[0][0] = 1

for i in range(n):
    for j in range(A+1):
        if j - ls[i] >= 0:
            dp[i+1][j] = (dp[i][j - ls[i]] + dp[i][j])%M
        else:
            dp[i+1][j] = (dp[i][j])%M
print((dp[-1][A])%M)


"""
部分和問題
n個の整数、総和がAのうち最小の整数の個数(各種1個)
"""
n, A = map(int,input().split())
ls = list(map(int,input().split()))
#Aは適宜最大値に変える
dp = [[0 for _ in range(A+1)] for __ in range(n+1)]
dp[0][0] = 0
for i in range(1,n+1):
    dp[0][i] = float("inf")

for i in range(n):
    for j in range(A+1):
        if j >= ls[i]:
            dp[i+1][j] = min(dp[i][j], dp[i][j-ls[i]]+1)
        else:
            dp[i+1][j] = dp[i][j]

if dp[-1][-1] == float('inf'):
    print(-1)
else:
    print(dp[-1][-1])



"""
LCS
"""
s1 = input()
s2 = input()

dp = [[0 for i in range(len(s2)+1)] for __ in range(len(s1)+1)]
dp[0][0]=0
for i in range(len(s1)):
    c1 = s1[i]
    for j in range(len(s2)):
        c2 = s2[j]
        if c1 == c2:
            dp[i+1][j+1]=max(dp[i][j]+1,dp[j+1][j],dp[i][j+1])
        else:
            dp[i+1][j+1]=max(dp[i+1][j],dp[i][j+1])
            
print(dp[-1][-1])

"""
最小コスト弾性マッチング問題
"""
m,n = map(int,input().split()) #lsa,lsbの長さ
# lsa = list(map(int,input().split()))
# lsb = list(map(int,input().split()))
cost = [list(map(int,input().split())) for _ in range(m)]

dp = [[float("inf") for i in range(m+1)] for __ in range(n+1)]
dp[0][0]=0

for i in range(m):
    for j in range(n):
        dp[i+1][j+1] = min(dp[i+1][j+1] + cost[i][j], dp[i][j+1] + cost[i][j], dp[i][j+1] + cost[i][j])
print(dp[-1][-1])


"""
レーベンシュタイン距離 (diffコマンド)
"""
s = input()
t = input()

dp = [[float("inf") for _ in range(len(t)+1)] for __ in range(len(s)+1)]
dp[0][0] = 0
for i in range(len(s)):
    for j in range(len(t)):
        if s[i] == t[j]:
            dp[i+1][j+1] = min(dp[i][j],dp[i][j+1]+1,dp[i+1][j]+1)
        else:
            dp[i+1][j+1] = min(dp[i][j]+1,dp[i][j+1]+1,dp[i+1][j]+1)
print(dp[-1][-1])



"""
LIS
各要素に対する最長増加部分列
"""
"""
LIS
各長さに対する最小の要素(こっちの方が速い場合が多い)
"""
#リストseqからLISの長さを出す
import bisect

LIS = [seq[0]]
for i in range(len(seq)):
    if seq[i] > LIS[-1]:
        LIS.append(seq[i])
    else:
        LIS[bisect.bisect_left(LIS, seq[i])] = seq[i]

print(len(LIS))




"""
発電計画問題
"""
t = int(input())
g = [list(map(int,input().split())) for _ in range(t)]

dp = [0 for _ in range(t+2)]

for i in range(2,t+2):
    for j in range(i-1):
        for k in range(j+1,i):
            dp[i] =  max(dp[i], dp[j] + g[j][k])
print(dp[t+1])


"""
分かち書き
"""
#あんま問題無さそう？
#https://qiita.com/drken/items/a5e6fe22863b7992efdb#%E5%88%86%E3%81%8B%E3%81%A1%E6%9B%B8%E3%81%8D



"""
分割数
dp[i][j]:=j のi 分割の総数
"""
n, m = map(int,input().split())
M = int(input())  #MOD

dp = [[0 for _ in range(n+1)] for __ in range(m+1)]

dp[0][0] = 1

for i in range(1,m+1):
    for j in range(1,n+1):
        #適宜MODで割る
        if j-i >= 0:
            dp[i][j] = dp[i][j-i] + dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])


"""
重複組み合わせ
dp[i+1][j]:=i 番目までの品物からj 個選ぶ組み合わせの総数
"""
n, m = map(int,input().split())
ls = list(map(int,input().split()))
M = int(input())  #MOD

dp = [[0 for _ in range(m+1)] for __ in range(n+1)]


for i in range(n+1):
    dp[i][0] = 1

for i in range(n):
    a = ls[i]
    for j in range(1,m+1):
        #適宜MODで割る
        if j-1-a >= 0:
            dp[i+1][j] = dp[i+1][j-1] +dp[i][j] - dp[i][j-1-a]
        else:
            dp[i+1][j] = dp[i+1][j-1] +dp[i][j] 

print(dp[-1][-1])


"""
連鎖行列積
"""
INF = 2000000000

def matrixChainMultiplication(m):
    global n
    for l in range(2, n+1):
        for i in range(1, n-l + 2):
            j = i + l - 1
            m[i][j] = INF
            for k in range(i, j):
                m[i][j] = min(m[i][j], m[i][k] + m[k+1][j]+p[i-1]*p[k]*p[j])
    return m
    
n = int(input())

m = [[0 for i in range(n + 1)] for j in range(n + 1)]
p = []

for i in range(n):
    input_command = input()
    num1,num2 = input_command.split()
    p.append(int(num1))
    if i == n-1:
        p.append(int(num2))
        
m = matrixChainMultiplication(m)
print(m[1][n])

"""
連鎖行列積2
"""
N = int(input())
R = [0]*N
C = [0]*N
for i in range(N):
    R[i], C[i] = map(int, input().split())

INF = 10**18
dp = [[INF]*N for i in range(N)]
for i in range(N):
    dp[i][i] = 0
for l in range(1, N):
    for i in range(N-l):
        a0 = R[i]
        c0 = C[i+l]
        dp[i][i+l] = min(a0*C[j]*c0 + dp[i][j] + dp[j+1][i+l] for j in range(i, i+l))
print(dp[0][N-1])

