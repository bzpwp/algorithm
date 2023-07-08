n,m = map(int,input().split())

x = m
y = 0
for i in range(n-1):
    x *= m-1
    y = x - y
    x %= 998244353

print(y%998244353)