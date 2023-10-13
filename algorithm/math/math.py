#約数
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

print(make_divisors(123464))



#素数判定
def trial_division(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(ceil(sqrt(n))) + 1, 2):
        if n % i == 0:
            return False
    return True

#素数列挙
def sieve_eratosthenes(n):
    primes = [0, 1] * (n // 2 + 1)
    if n % 2 == 0:
        primes.pop()
    primes[1] = 0
    primes[2] = 1
    for p in range(3, int(n ** 0.5) + 1, 2):
        if primes[p]:
            for q in range(p * p, n + 1, 2 * p):
                primes[q] = 0
    return primes

#素数列挙その2
import numpy as np
 
def sieve_eratosthenes(n):
    primes = np.zeros(n + 1, dtype=np.bool)
    primes[2] = 1
    primes[3::2] = 1
    for p in range(3, int(n ** 0.5) + 1, 2):
        if primes[p]:
            primes[p * p::2 * p] = 0
    return primes


#素因数分解
#約数の個数
"""nを素因数分解"""
"""2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

factorization(24) 
## [[2, 3], [3, 1]] 
##  24 = 2^3 * 3^1

#約数の個数
#上の結果を使う


#約数の合計
import math
def divisor_s(n):
   sigma=0
   for s in range(1,n+1):
       for t in range(1,s+1):
           sigma+=math.cos(2*math.pi*t*n/s)
   return int(round(sigma,0))
divisor_s(1200)
#3844


#約数とその組の列挙
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


#逆元
pow(38, -1, 97)
#mod97における38の逆元


#nCr
def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

p = 10 ** 9 + 7
N = 10 ** 6  # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用
 
for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

print(cmb(n, r, p))

#高速累乗計算
def pow_k(x, n):
    """
    O(log n)
    """
    if n == 0:
        return 1

    K = 1
    while n > 1:
        if n % 2 != 0:
            K *= x
        x *= x
        n //= 2

    return K * x


#高速累乗計算(mod)
def pow_k(x, n, mod):
    """
    O(log n)
    """
    if n == 0:
        return 1

    K = 1
    while n > 1:
        if n % 2 != 0:
            K = K * x % mod
        x = x * x % mod
        n //= 2

    return K * x

# 行列累乗



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


//　行列計算の順番によって答えが変わる
// 上の例だと、正方形の右側に縦一列の行列がある
// 正方形の中で入力が横、出力が縦のイメージ。行列の順番が逆
//　だと逆になる

print(ret[0][0])
