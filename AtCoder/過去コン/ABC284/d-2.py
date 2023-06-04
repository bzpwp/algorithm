import math

# エラトステネスの篩
def prime(n):
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(2 * i, n + 1, i):
                is_prime[j] = False
    return is_prime

# 素数列挙
# N = 10000
N = 3*10**9
# M以下の整数の素数判定
prime = prime(N)


# 素数判定を基に, 素数リストを作成
prime_list = []
for i in range(N + 1):
    if prime[i]:
        prime_list.append(i)
        
# print(len(prime_list))
# print(prime_list)
t = int(input())


import math
from collections import Counter

# 素因数分解を行う関数
def prime_factorization(n):
    # Counterクラスを呼び出してオブジェクト生成
    counter = Counter()
    
    # 素数で割り切れるかの判定
    for p in prime_list:
        # １回割り切れるごとに+1カウントしていく
        while n % p == 0:
            counter[p] += 1
            n //= p
    # n が1より大きい数字として残っていれば、素数
    if n != 1:
        counter[n] += 1
    return counter

# N = int(input())
# result = prime_factorization(N)
# for key, value in result.items():
#     for i in range(value):
#         print(key, end = " ")

for i in range(t):
    n = int(input())
    c = prime_factorization(n)
    for j in c:
        if c[j]==1:
            q = j
        else:
            p = j
    print(p,q)