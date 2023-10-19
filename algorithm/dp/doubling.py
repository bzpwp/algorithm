"""
https://drken1215.hatenablog.com/entry/2021/10/08/231200
きたまさ法(参考)
https://misawa.github.io/others/fast_kitamasa_method.html
"""
# MOD
MOD = 1000000007

# N の対数
LOG = 62

# 入力
N, B, K = map(int, input().split())
C = list(map(int, input().split()))

# dp[i] と dp[j] を掛け合わせて dp[i+j] を得る関数
# tj: 10^j を B で割ったあまり
def mul(dpi, dpj, tj):
    res = [0] * B
    for p in range(B):
        for q in range(B):
            res[(p * tj + q) % B] += dpi[p] * dpj[q]
            res[(p * tj + q) % B] %= MOD
    return res

# ten[i]: 10^(2^i) を B で割ったあまり
ten = [10] * LOG
for i in range(1, LOG):
    ten[i] = (ten[i - 1] * ten[i - 1]) % B

# dp[2^i][r] を doubling[i][r] と書くことにする
doubling = [[0] * B for _ in range(LOG)]

# 初期化 (doubling[0] = dp[1])
for k in range(K):
    doubling[0][C[k] % B] += 1

# ダブリング
for i in range(1, LOG):
    doubling[i] = mul(doubling[i - 1], doubling[i - 1], ten[i - 1])

# ダブリングした結果をもとに答えを求める
res = [0] * B
res[0] = 1
for i in range(LOG):
    if N & (1 << i):
        res = mul(res, doubling[i], ten[i])
print(res[0])