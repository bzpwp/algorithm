n = int(input())
num1=[1,1,1,1,1,1,1,1,1]
for a in range(n-1):
    num = num1
    num1[0]+=num[1]
    num1[8]+=num[7]
    for a in range(1,8): #1~7
        num1[a]+=num[a-1]
        num1[a]+=num[a+1]
print(sum(num1)%998244353)
print(num1)