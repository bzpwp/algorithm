n = int(input())
ls = list((map(int,input().split())))
from collections import defaultdict

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

dd = defaultdict(list)
prime_check = False
m2 = 10**18
M2 = 0
m3 = 10**18
M3 = 0



ls2 = factorization(ls[0])
for j in ls2:
    x,y = j
    if x == 2:
        m2 = min(m2,y)
        M2 = max(M2,y)
    elif x == 3:
        m3 = min(m3,y)
        M3 = max(M3,y)
    elif x == 1:
        dd[1]=1
        m2 = 0
        m3 = 0
    else:
        dd[x]=y

ans = 0

for i in ls[1:]:
    ls2 = factorization(i)
    for j in ls2:
        x,y = j
        if x == 2:
            m2 = min(m2,y)
            M2 = max(M2,y)
        elif x == 3:
            m3 = min(m3,y)
            M3 = max(M3,y)
        elif x == 1:
            dd[1]=1
            m2 = 0
            m3 = 0
        else:
            if x not in dd:
                print(-1)
                exit()
            elif y != dd[x]:
                print(-1)
                exit()
