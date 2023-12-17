ls = [list(map(int,input().split())) for _ in range(9)]
c = set(list(range(1,10)))
for i in range(9):
    s = set(ls[i])
    if s != c:
        print("No")
        exit()

for i in range(9):
    s = set([ls[j][i] for j in range(9)])
    if s != c:
        print("No")
        exit()


for i in range(3):
    for j in range(3):
        s = [3*i, 3*j]
        sc = []
        for k in range(3):
            for l in range(3):
                sc.append(ls[s[0]+k][s[1]+l])
        sc = set(sc)
        if sc != c:
            print("No")
            exit()
print("Yes")