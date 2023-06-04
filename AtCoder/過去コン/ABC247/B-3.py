n = int(input())
ls = []
for i in range(n):
    ls.append(list(input().split()))

ls1 = []
ls2 = []

for a in ls:
    ls1.append(a[0])
for a in ls:
    ls2.append(a[1])
print(ls1)
print(ls2)
for a in range(n-1):
    print(ls1[a+1:n])
    if ls1[a] not in ls1[a+1:n] and  ls1[a] not in ls2[a+1:n]:
        continue
    elif ls2[a] not in ls1[a+1:n] and  ls2[a] not in ls2[a+1:n]:
        continue
    else:
        print("No")
        exit()
print("Yes")