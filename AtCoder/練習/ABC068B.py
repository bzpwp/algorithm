n = int(input())
x = 2
a = 1
while a > 0: #一般的な制約で解きたかっただけ
    if x >100:
        break
    x = x*2
    a +=1
for i in range(a+1):
    if 2**i <= n < 2**(i+1):
        print(2**i)