n = int(input())
num1=[1,1,1,1,1,1,1,1,1]
for a in range(n-1):
    num = num1
    num1 = [(num[0]+num[1])%998244353,(num[0]+num[1]+num[2])%998244353,(num[3]+num[1]+num[2])%998244353,(num[3]+num[4]+num[2])%998244353,(num[3]+num[4]+num[5])%998244353,(num[6]+num[4]+num[5])%998244353,(num[6]+num[7]+num[5])%998244353,(num[7]+num[8]+num[6])%998244353,(num[7]+num[8])%998244353]
print(sum(num1)%998244353)