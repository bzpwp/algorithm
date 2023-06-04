n,k = map(int, input().split())
lsa = list(map(int, input().split()))
lsb = list(map(int, input().split()))


y = max(lsa)
z = [i for i, x in enumerate(lsa) if x == y]
for i in z:
    if i+1 in lsb:
        print("Yes")
        exit()

print("No")