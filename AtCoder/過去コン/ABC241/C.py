n = int(input())
ls = [input() for _ in range(n)]
import sys
for a in ls:
    if a.count('.') <= 2:
        print("Yes")
        sys.exit()

for a in range(n):
    x = 0
    for b in ls:
        if b[a] == ".":
            x += 1
    if x <= 2:
        print("Yes")
        sys.exit()

x = 0
for a in range(n):
    if ls[a][a]==".":
        x += 1
if x <= 2:
        print("Yes")
        sys.exit()

x = 0
for a in range(n):
    if ls[a][n-a-1]==".":
        x += 1
if x <= 2:
        print("Yes")
        sys.exit()
        
print("No")