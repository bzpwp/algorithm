a,b = map(int,input().split())

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

# print(cmb(n, r, p))

if a/b < 1/2:
    print(0)
elif a/b > 2:
    print(0)
else:
    if a > b:
        a,b  =b,a
    dif = b-a
    if (a-dif)%3 != 0:
        print(0)
    else:
        x = (a-dif)//3
        y = x + dif
        print(cmb(x+y, x, p))
