n = int(input())
la = list(map(int,input().split()))
m = int(input())
lb = list(map(int,input().split()))
x = int(input())

num = x//la[0]

d = [0 for i in range(x+1)]

for i in lb:
    d[i] = -1

dp = [d for __ in range(num+1)]

dp[0][0] = 1

for i in range(num):
    for j in range(x+1):
        