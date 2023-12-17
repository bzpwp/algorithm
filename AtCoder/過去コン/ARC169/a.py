n = int(input())
al = list(map(int,input().split()))
pl = list(map(int,input().split()))

def matrix_multi(a: list, b: list) -> list:
    len_a, len_b, len_b_zero = len(a), len(b), len(b[0])
    c = [[0] * len(b[0]) for _ in range(len_a)]
    for i in range(len_a):
        for j in range(len_b_zero):
            for k in range(len_b):
                c[i][j] += a[i][k] * b[k][j]

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



fibonacci = [[0 for _ in range(n)] for __ in range(n)]
for i in range(n):
    fibonacci[i][i] = 1
# print(fibonacci)
for i in range(n-1):
    fibonacci[i+1][pl[i]-1] += 1
# print(fibonacci)
fibonacci = matrix_pow(fibonacci, 10**100)
# print(fibonacci)
x = 0
for i in range(n):
    x += al[i]*fibonacci[i][0]
if x < 0:
    print("-")
elif x == 0:
    print(0)
elif x > 0:
    print("+")