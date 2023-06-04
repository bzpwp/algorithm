n = int(input())
ls = []
for i in range(10**9+1):
    ls.append([])
for i in range(n):
    x,y = map(int, input().split())
    ls[y].append([x,i])
s = input()
for i in range(10**9+1):
    if ls[i]==[]:
        continue
    else:
        ls[i].sort()
        lg = len(ls[i])
        if lg == 1:
            continue
        for a in range(lg-1):
            if s[ls[i][a][1]]=="R":
                for b in range(a+1,lg):
                    if s[ls[i][b][1]]=="L":
                        print("Yes")
                        exit()
print("No")