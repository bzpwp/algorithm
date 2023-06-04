MOD = 998244353

def main():
    N, M, K = map(int, input().split())
    dp = [[0] * (M) for _ in range(N)]
    for l in range(M):
        dp[0][l] = 1

    for i in range(N-1):
        for j in range(M):
            for k in range(-1*K, K+1):
                print(j,k)
                if not(j+k >=0 and j+k <=M-1):
                    dp[i+1][j] += dp[i][j+k]
                    dp[i+1][j] %= MOD
                print(dp)
    print(sum(dp[-1]) % MOD)

if __name__ == '__main__':
    main()