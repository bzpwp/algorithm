n = int(input())
ls = list(map(int,input().split()))
import copy
check = copy.copy(ls)
B = sorted(ls, reverse=True)

order = []
for i in range(n):
    ind = check.index(B[i])
    check[ind] = 10**5
    order.append(ind)

ok = 0
ng = 5000*5000+1
import math

def func(j): #個]
    choice = order[:j]
    choice.sort()
    S = sum([(0.9**j-i)*ls[choice[i]] for i in range(1,j+1)])
    return (S/(10-10*(0.9**j)))-1200/math.sqrt(k)

while ng-ok >=10**(-6):
    s = (ok+ng)/2
    boo = False
    for k in range(1,n+1): #k個選択
        if func(k) >= s:
            boo = True
    if boo:
        ok = s
    else:
        ng = s
print(ok)
