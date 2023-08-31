p, q = map(int, input().split())
a = list(map(int, input().split()))
a = [0] + a + [p+1]

# dp[i][j], 0<=i<=Q, 1<=j<=Q+1 (j=0は使わない), i<j
dp = [['']*(q+2) for _ in range(q+1)]
## 初期化 (間に解放対象がいないなら金貨ゼロ枚)
for i in range(q+1):
  dp[i][i+1] = 0
  
for n in range(1, q+1):
  # n=ブロック内の解放対象人数
  # i,j=ブロック(左端,右端)の部屋番号
  # j = i+n+1 < q+2
  for i in range(q-n+1):
    j = i + n + 1
    
    t = float('inf')
    for k in range(i+1, j):
      # 1人開放すればブロック数が小さいdpに帰着
      # →1人開放する方法の最小値が今のブロック数の答え
      t = min(t, dp[i][k]+dp[k][j])
    
    # ①1人解放したブロックのコスト + ②1人開放するコスト
    # ②=(a[j]-1) - a[i] - 1(解放した1人の分)
    dp[i][j] = t + a[j] - a[i] - 2
print(a)
print(dp[0][q+1])   