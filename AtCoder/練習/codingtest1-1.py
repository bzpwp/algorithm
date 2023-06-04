l,r = map(int, input().split())
m = int(input())
ls1 = list(map(int,input().split()))

if 1 in ls1:
    print(0)
else:
    ls2 = [i for i in range(l,r+1)] #モンスターのレベルリスト
    for a in ls1:
        for b in ls2:
            if b%a==0:
                ls2.remove(b)
    print(len(ls2))
