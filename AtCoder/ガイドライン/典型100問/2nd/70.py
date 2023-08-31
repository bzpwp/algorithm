
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
a,b = map(int,input().split())
print(pow_k(a,b,1000000007))