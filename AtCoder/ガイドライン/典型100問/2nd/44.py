def func(n):
    return int(n*(n+1)*(n+2)/6)

odd = []
all = []
n = 0
while func(n) <= 10**6:
    n += 1
    x = func(n)
    all.append(x)
    if x%2 == 1:
        odd.append(x)

all.pop()
odd.pop()

dp = [i for i in range(10**6+1)]
dp2 = [i for i in range(10**6+1)]
for i in all:
    for j in range(10**6+1-i):
        dp[j+i] = min(dp[j+i],dp[j]+1)

for i in odd:
    for j in range(10**6+1-i):
        dp[j+i] = min(dp[j+i],dp[j]+1)

n = int(input())
print(dp[n], dp2[n])