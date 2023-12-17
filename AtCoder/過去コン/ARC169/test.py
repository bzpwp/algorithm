def matrix_multi(a: list, b: list) -> list:
    len_a, len_b, len_b_zero = len(a), len(b), len(b[0])
    c = [[0] * len(b[0]) for _ in range(len_a)]
    for i in range(len_a):
        for j in range(len_b_zero):
            for k in range(len_b):
                c[i][j] += a[i][k] * b[k][j]
                c[i][j] %= mod

    return c


def matrix_pow(a: list, n: int) -> list:
    len_a = len(a)
    cnt = [[0] * len_a for _ in range(len_a)]

    for i in range(len_a):
        cnt[i][i] = 1

    while n > 0:
        if n & 1:
            cnt = matrix_multi(a, cnt)

        a = matrix_multi(a, a)
        n >>= 1

    return cnt


n = int(input())
mod = 998244353

fibonacci = [[1, 1,3], [1,3, 0],[3,4,5]]
fibonacci = matrix_pow(fibonacci, n)
print(fibonacci)
ans = fibonacci[1][0]
# print(*fibonacci, sep="\n")
print(ans)