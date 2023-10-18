n,l = map(int,input().split())
k = int(input())
ls = [0] + list(map(int,input().split()))
# import itertools
acc = [ls[i+1] - ls[i] for i in range(n)]
acc.sort()
print(acc)
ok = 0
ng = n
while ng-ok>1:
    s = (ok+ng)//2
    A = 0
    B = 0
    C = acc[s]
    for i in ls:
        B += i
        if B>=C:
            A += 1
            C = B+acc[s]
    if A >= k+1:
        ok = s
    else:
        ng = s
    # print(ok)
print(acc[ok]) 