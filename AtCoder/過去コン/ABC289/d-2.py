n = int(input())
la = list(map(int,input().split()))
m = int(input())
lb = list(map(int,input().split()))
x = int(input())

dp = [0 for i in range(x+1)]

for i in lb:
    dp[i] = -1

dp[0] = 1
for i in range(x+1):
    if dp[i] > 0:
        for j in la:
            if i+j <=x and dp[i+j] >= 0:
                dp[i+j] = 1
if dp[-1]:
    print("Yes")
else:
    print("No")