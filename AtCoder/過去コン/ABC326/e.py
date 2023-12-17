n = int(input())
ls = list(map(int,input().split()))
# ls.sort()
M = 998244353
S = 0
X = 0
mother = pow(n, -1, M)
for i in range(n):
    x = mother*ls[i]
    x += S
    x %= M
    S += pow(n, -1, M)*x
    X += pow(n, -1, M)*x*(i+1)
    S%=M
    X%=M
    print()
print(X)