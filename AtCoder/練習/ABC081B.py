n = int(input())
ls1 = list(map(int, input().split()))
ls2 = []
x = 0
for c in ls1:
    while c%2 ==0:
        x += 1
        c = c/2
    ls2.append(x)
    x = 0
print (min(ls2))
