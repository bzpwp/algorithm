n = int(input())
ls = []
for i in range(n):
    ls.append(list(input().split()))
print(ls)
for a in range(n-1):
    for b in range(a+1,n):
        if b == a:
            print("No")
            exit()
        elif b == [a[1],a[0]]:
            print("No")
            exit()
print("Yes")