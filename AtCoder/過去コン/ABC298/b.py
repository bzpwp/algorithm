n = int(input())

lsa = []
for i in range(n):
    a = list(map(int,input().split()))
    for j in range(n):
        if a[j] == 1:
            lsa.append([i+1,j+1])

lsb = []

for i in range(n):
    b = list(map(int,input().split()))
    for j in range(n):
        if b[j] == 1:
            lsb.append([i+1,j+1])
if all(x in lsb for x in lsa):
    print("Yes")
    exit()

for i in range(3):
    lsa = [[n+1-j,i] for i, j in lsa]
    lsa.sort()
    if all(x in lsb for x in lsa):
        print("Yes")
        exit()

print("No")