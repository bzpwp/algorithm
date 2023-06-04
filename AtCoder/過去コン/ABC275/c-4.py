pone = []
for i in range(9):
    s = input()
    for j in range(9):
        if s[j]=="#":
            pone.append([i,j])


import itertools
x = len(pone)
ans = 0
choice = list(itertools.combinations(list(range(x)),4))
c = list(itertools.combinations(list(range(4)),2))

for i in choice:
    ls = []
    p1 = pone[i[0]]
    x1,y1 = p1
    p2 = pone[i[1]]
    x2,y2 = p2
    p3 = pone[i[2]]
    x3,y3 = p3
    p4 = pone[i[3]]
    x4,y4 = p4
    d1 = (x1-x2)**2+(y1-y2)**2
    d2 = (x1-x3)**2+(y1-y3)**2
    d3 = (x1-x4)**2+(y1-y4)**2
    d4 = (x2-x3)**2+(y2-y3)**2
    d5 = (x2-x4)**2+(y2-y4)**2
    d6 = (x3-x4)**2+(y3-y4)**2
    if d1==d2:
        if d1 == d5 and d1 == d6:
            ans += 1
    elif d2==d3:
        if d2 == d4 and d2 == d5 :
            ans += 1
    elif d3 == d1:
        if d3==d4 and d3==d6:
            ans += 1

print(ans)