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


"""
数列の一般項など
https://atcoder.jp/contests/abc009/submissions/175601
"""


import sys

def prob_d():
  def v_mul_mat(vec, mat):
    l = len(vec)
    ret = [0] * l
    for i in range(l):
      s = 0
      for j in range(l):
        s ^= vec[j] & mat[j][i]
      ret[i] = s
    return ret

  def mat_mulv(mat, vec):
    l = len(mat)
    ret = [0] * l
    for i in range(l):
      v = mat[i]
      s = 0
      for j in range(l):
        s ^= v[j] & vec[j]
      ret[i] = s
    return ret

  def mat_mulv_sparse(vec, mat):
    ret = [mat[-1][i] & vec[-1] for i in range(len(vec))]
    for i in range(1, len(vec)):
      ret[i] ^= (mat[i-1][i] & vec[i-1])
    return ret

  def mat_exp(mat, ex):
    l = len(mat)
    ret = [0] * l
    ret[0] = 0xFFFFFFFF

    A = [v[:] for v in mat]
    while ex:
      if ex & 1:
        ret = v_mul_mat(ret, A)
      next_A = [None] * l
      next_A[0] = v_mul_mat(A[0], A)
      for i in range(1, l):
        next_A[i] = mat_mulv_sparse(next_A[i-1], mat)
      A = next_A
      ex >>= 1
    ret2 = [None] * l
    ret2[0] = ret
    for i in range(1, l):
      ret2[i] = mat_mulv_sparse(ret2[i-1], mat)
    return ret2

  stdin = sys.stdin
  K, M = map(int, stdin.readline().split())
  As = list(map(int, stdin.readline().split()))
  Cs = list(map(int, stdin.readline().split()))

  mat = [[0] * K for _ in range(K)]
  for i in range(K - 1):
    mat[i][i+1] = 0xFFFFFFFF
  mat[K-1] = Cs[::-1]

  M -= 1

  mat = mat_exp(mat, M)
  vec = mat_mulv(mat, As)
  print(vec[0])

prob_d()

"""
数列の一般項など
https://tjkendev.github.io/procon-library/python/series/fibonacci.html
"""
# O(N)
def fibonacci1(N, M):
    a = 0; b = 1
    for _ in range(N):
        a, b = b, (a + b) % M
    return a

# O(log N)
def fibonacci2(N, M):
    # R = [1, 0; 0, 1]
    RA = RD = 1; RB = RC = 0
    # X = [1, 1; 1, 0]
    XA = XB = XC = 1; XD = 0
    while N:
        if N & 1:
            # R <- RX
            RA, RB, RC, RD = (RA*XA + RB*XC) % M, (RA*XB + RB*XD) % M, (RC*XA + RD*XC) % M, (RC*XB + RD*XD) % M
        # X <- XX
        XA, XB, XC, XD = (XA**2 + XB*XC) % M, XB*(XA + XD) % M, XC*(XA + XD) % M, (XB*XC + XD**2) % M
        N >>= 1
    return RC


"""
数列の一般項など
https://scrapbox.io/kyopuro-ryusuke920/%E8%A1%8C%E5%88%97%E7%B4%AF%E4%B9%97
"""
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

fibonacci = [[1, 1], [1, 0]]
fibonacci = matrix_pow(fibonacci, n)

ans = fibonacci[1][0]
# print(*fibonacci, sep="\n")
print(ans)


"""
きたまさ法 (Kitamasa Method)
https://tjkendev.github.io/procon-library/python/series/kitamasa.html
"""

