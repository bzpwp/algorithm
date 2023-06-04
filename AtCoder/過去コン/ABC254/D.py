n = int(input())

import math
# x = math.floor(math.sqrt(n**2))

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

y = 1
for i in range(2,n+1):
    z = 1
    ls = factorization(i)
    print(ls)
    for l in ls:
        if l[0]<=n:
            z *= l[1]
    print(z)
    y += z
print(y)
