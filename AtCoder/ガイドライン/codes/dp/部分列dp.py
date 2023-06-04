#https://qiita.com/drken/items/a207e5ae3ea2cf17f4bd

"""
部分文字列の数え上げ
"""
MOD = 1000000007

# res[i][c] := i 文字目以降で最初に文字 c が登場する index (存在しないときは n)
def calcNext(S: str):
    n = len(S)
    res = [[n] * 26 for _ in range(n+1)]
    for i in range(n-1, -1, -1):
        for j in range(26):
            res[i][j] = res[i+1][j]
        res[i][ord(S[i]) - ord('a')] = i
    return res

# mod 1000000007 の世界で a += b する関数
def add(a: int, b: int) -> int:
    return (a + b) % MOD

# メイン処理
if __name__ == '__main__':
    # 入力
    S = input().strip()
    n = len(S)

    # 前処理配列
    next = calcNext(S)

    # DP
    dp = [0] * (n+1)
    dp[0] = 1  # 初期化、空文字列 "" に対応
    for i in range(n):
        for j in range(26):
            if next[i][j] >= n:
                continue  # 次の文字 j がもうない場合はスルー
            dp[next[i][j] + 1] = add(dp[next[i][j] + 1], dp[i])

    # 集計
    res = sum(dp) % MOD

    print(res)


"""
回文部分文字列の数え上げ
"""

MOD = 10 ** 9 + 7

# res[i][c] := i 文字目以降で最初に文字 c が登場する index (存在しないときは n)
def calcNext(S: str) -> list:
    n = len(S)
    res = [[n] * 26 for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(26):
            res[i][j] = res[i + 1][j]
        res[i][ord(S[i]) - ord('a')] = i
    return res

def add(a: int, b: int) -> int:
    return (a + b) % MOD

S = input()
n = len(S)
T = S[::-1]

ns = calcNext(S)
nt = calcNext(T)
dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        for k in range(26):
            ni = ns[i][k]
            nj = nt[j][k]
            if ni + nj + 2 > n:
                continue
            dp[ni + 1][nj + 1] = add(dp[ni + 1][nj + 1], dp[i][j])

res = 0
for i in range(n + 1):
    for j in range(n - i + 1):
        num = 1
        for k in range(26):
            if ns[i][k] + 1 + j <= n:
                num += 1
        res = (res + dp[i][j] * num) % MOD

print(res - 1)




"""
最短の非部分文字列
"""




"""
部分文字列の辞書順
"""