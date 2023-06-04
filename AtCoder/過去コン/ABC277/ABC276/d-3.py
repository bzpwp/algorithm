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

ls2 = factorization(ls[0])
for j in ls2:
    x,y = j
    if x == 2:
        dd[2].append(y)
    elif x == 3:
        dd[3].append(y)
    elif x == 1:
        dd[1]=[1]
        dd[2].append(0)
        dd[3].append(0)
    else:
        dd[x]=y


for i in ls[1:]:
    ls2 = factorization(i)
    for j in ls2:
        x,y = j
        if x == 2:
            dd[2].append(y)
        elif x == 3:
            dd[3].append(y)
        elif x == 1:
            dd[1]=[1]
            dd[2].append(0)
            dd[3].append(0)
        else:
            if x not in dd:
                print(-1)
                exit()
            elif y != dd[x]:
                print(-1)
                exit()
                
ans = 0
if dd[2]!=[]:
    m2 = min(dd[2])
    for i in dd[2]:
        ans += i-m2
if dd[3]!=[]:
    m3 = min(dd[3])
    for i in dd[3]:
        ans += i-m3

print(ans)