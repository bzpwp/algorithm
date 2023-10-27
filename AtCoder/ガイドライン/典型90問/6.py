n,k = map(int,input().split())
S = input()

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
    # S = input().strip()
    n = len(S)

    # 前処理配列
    next = calcNext(S)
    # print(next)
    # DP
    dp = [0] * (n+1)
    dp[0] = 1  # 初期化、空文字列 "" に対応
    for i in range(n):
        for j in range(26):
            if next[i][j] >= n:
                continue  # 次の文字 j がもうない場合はスルー
            dp[next[i][j] + 1] = dp[next[i][j] + 1] + dp[i]
    print(dp)
    # 集計
    res = sum(dp) % MOD

    print(res)
