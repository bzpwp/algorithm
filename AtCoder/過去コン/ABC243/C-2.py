n = int(input())
import sys
ls = []
for i in range(10**9+1):
    ls.append([])
for i in range(n):
    x,y = map(int, input().split())
    ls[y].append([x,i])
s = input()
for i in range(10**9+1):
    lss = ls[i]
    lg = len(lss)
    if lg == 0 or lg == 1:
        continue
    else:
        lss.sort()
        for a in range(lg-1):
            if s[lss[a][1]]=="R":
                for b in range(a+1,lg):
                    if s[lss[b][1]]=="L":
                        print("Yes")
                        sys.exit()
print("No")