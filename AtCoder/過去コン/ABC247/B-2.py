n = int(input())
ls = []
for i in range(n):
    ls.append(list(input().split()))

nl = []

for a in range(n-1):
    for b in range(a+1,n):
        if ls[a][0] == ls[b][0]:
            for c in range(a+1,n):
                if ls[a][1] == ls[c][0]:
                    for d in range(a+1,n):
                        if ls[a][1] == ls[b][1]:
                            print("No")
                            exit()
print("Yes")