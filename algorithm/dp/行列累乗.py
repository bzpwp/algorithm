"""
数列の一般項など
https://qiita.com/ophhdn/items/e6451ec5983939ecbc5b
"""




def mat_mul(a, b) :
    I, J, K = len(a), len(b[0]), len(b)
    c = [[0] * J for _ in range(I)]
    for i in range(I) :
        for j in range(J) :
            for k in range(K) :
                c[i][j] += a[i][k] * b[k][j]
            c[i][j] %= m
    return c


def mat_pow(x, n):
    y = [[0] * len(x) for _ in range(len(x))]

    for i in range(len(x)):
        y[i][i] = 1

    while n > 0:
        if n & 1:
            y = mat_mul(x, y)
        x = mat_mul(x, x)
        n >>= 1

    return y


l, a, b, m = LI()
d0 = 0
ret = [[0], [a], [1]]
for i in range(1, 19):
    if 10 ** i - 1 - a < 0:
        continue
    d1 = min((10 ** i - 1 - a) // b + 1, l)
    mat = [[10 ** i, 1, 0], [0, 1, b], [0, 0, 1]]
    ret = mat_mul(mat_pow(mat, d1 - d0), ret)
    if d1 == l:
        break
    d0 = d1


print(ret[0][0])
