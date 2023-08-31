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

ps = sieve_eratosthenes(10**5+1)
like = [0 for _ in range(10**5+1)]
for i in range(3,10**5+2):
    if ps[i] and ps[(i+1)//2]:
        like[i] = 1
import itertools

like = list(itertools.accumulate(like))

q = int(input())
for i in range(q):
    l,r = map(int,input().split())
    print(like[r] - like[l-1])