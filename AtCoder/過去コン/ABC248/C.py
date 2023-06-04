n,m,k = map(int, input().split())
S = 998244353

import functools as ft


def permutation(n, k):
    if k > n:
        return 0
    elif 0 < k <= n:
        return ft.reduce(lambda x, y:x * y, [n - v for v in range(k)])
    else:
        return 1


def factorial(n):
    return permutation(n, n - 1)


def combination(n, k):
    return int(permutation(n, k) / factorial(k))


def homogeneous(n, k):
    return combination(n + k - 1, k)


def homogeneous_with_limit(m, n, t):
    return sum([(-1)**k * combination(n, k) * homogeneous(n, t - n - m * k) \
                for k in range(0, int((t - n) / m) + 1)])


x = 0
for i in range(k-n+1):
    x += homogeneous_with_limit(m-1, n, i)
    if x > S:
        x = x%S
print(x)