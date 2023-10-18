n,l = map(int,input().split())
k = int(input())
ls = list(map(int,input().split())) + [l]


import copy
ok = 0
ng = l+1

while ng-ok>1:
# for _ in range(2):
    s = (ok+ng)//2
    A = 0
    # acc = 0
    C = copy.copy(s)
    for i in range(n+1):
        # acc += ls[i]
        if ls[i] >= C:
            A += 1
            C = s + ls[i]
            print(A,C,"!")
    if A >= k+1:
        ok = s
    else:
        print(A,"A")
        ng = s
    print(ok,ng)
# print(ng,ok)
print(ok) 