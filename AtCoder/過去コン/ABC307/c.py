ha,wa = map(int,input().split())
A = [list(input()) for _ in range(ha)]

hb,wb = map(int,input().split())
B = [list(input()) for _ in range(hb)]

hx,wx = map(int,input().split())
X = [list(input()) for _ in range(hx)]

from collections import defaultdict


Ablack = defaultdict(set)
for i in range(ha):
    for j in range(wa):
        if A[i][j] == "#":
            Ablack[i].add(j)
    
Bblack = defaultdict(set)
for i in range(hb):
    for j in range(wb):
        if B[i][j] == "#":
            Bblack[i].add(j)

Xblack = defaultdict(set)
for i in range(hx):
    for j in range(wx):
        if X[i][j] == "#":
            Xblack[i].add(j)

Amin_key = min(Ablack.keys(), default=None)
Amin_val = min(Ablack[Amin_key])

Bmin_key = min(Bblack.keys(), default=None)
Bmin_val = min(Bblack[Bmin_key])

Xmin_key = min(Xblack.keys(), default=None)
Xmin_val = min(Xblack[Xmin_key])

mvy = Xmin_key - Amin_key
mvx = Xmin_val - Amin_val

new_Ablack = defaultdict(set)
for i in Ablack:
    for j in Ablack[i]:
        new_Ablack[i+mvy].add(j+mvx)

import copy

for i in Xblack:
    for j in Xblack[i]:
        new_Xblack = copy.deepcopy(new_Ablack)
        b_mvy = i - Bmin_key
        b_mvx = j - Bmin_val
        for k in Bblack:
            for l in Bblack[k]:
                new_Xblack[k+b_mvy].add(l+b_mvx)
        if new_Xblack == Xblack:
            print("Yes")
            exit()


mvy = Xmin_key - Bmin_key
mvx = Xmin_val - Bmin_val

new_Bblack = defaultdict(set)
for i in Bblack:
    for j in Bblack[i]:
        new_Bblack[i+mvy].add(j+mvx)

import copy

for i in Xblack:
    for j in Xblack[i]:
        new_Xblack = copy.deepcopy(new_Bblack)
        a_mvy = i - Amin_key
        a_mvx = j - Amin_val
        for k in Ablack:
            for l in Ablack[k]:
                new_Xblack[k+a_mvy].add(l+a_mvx)
        if new_Xblack == Xblack:
            print("Yes")
            exit()

print("No")