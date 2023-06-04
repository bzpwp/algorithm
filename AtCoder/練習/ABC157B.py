lsa = []
for i in range(3):
    lsa.append(list(map(int,input().split())))
n = int(input())
lsb = [int(input()) for _ in range(n)]

import sys
for a in lsa:
    x = 0
    for b in a:
        if b in lsb:
            x += 1
    if x ==3:
        print("Yes")
        sys.exit()
for b in range(3):
    x =0
    for a in lsa:
        if a[b] in lsb:
            x += 1
    if x ==3:
        print("Yes")
        sys.exit()
x = 0
if lsa[0][0] in lsb and lsa[1][1] in lsb and lsa[2][2] in lsb:
    print("Yes")
    sys.exit()
if lsa[0][2] in lsb and lsa[1][1] in lsb and lsa[2][0] in lsb:
    print("Yes")
    sys.exit()

print("No")