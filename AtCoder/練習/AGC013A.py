n = int(input())
ls = list(map(int, input().split()))
x = 1
for a in range(1,len(ls)):
    if ls[a-1]<ls[a]: #増加
        for b in range(a+1,len(ls)):
            if ls[b-1]>ls[b]:
                print(b)
                x += 1
                ls = ls[b:]
                break
    if ls[a-1]>ls[a]: #減少
        for b in range(a+1,len(ls)):
            if ls[b-1]<ls[b]:
                print(b)
                x += 1
                ls = ls[b:]
                break
print(x)
