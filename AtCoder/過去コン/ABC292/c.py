n = int(input())

from collections import Counter

# 素因数分解を行う関数
def prime_factorization(n):
    # Counterクラスを呼び出してオブジェクト生成
    counter = Counter()
    
    # 素数で割り切れるかの判定
    for p in range(2, int(n ** 0.5) + 1):
        # １回割り切れるごとに+1カウントしていく
        while n % p == 0:
            counter[p] += 1
            n //= p
    # n が1より大きい数字として残っていれば、素数
    if n != 1:
        counter[n] += 1
    return counter

def num(N):
    result = prime_factorization(N)
    tot = 1
    for key, value in result.items():
        tot *= value + 1
    return tot





A = 0

if n%2==0:
    x = n//2
    A += num(x)**2
    x -= 1

B = 0

if n%2 == 1:
    x = n//2

for i in range(1,x+1):
    B += (num(i)*num(n-i))*2

print(A+B)