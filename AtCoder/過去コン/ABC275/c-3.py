pone = []
for i in range(9):
    s = input()
    for j in range(9):
        if s[j]=="#":
            pone.append([i,j])


import itertools
d = len(pone)
ans = 0
choice = list(itertools.combinations(list(range(d)),4))
c = list(itertools.combinations(list(range(4)),2))
def cal(a,b):
    x1, y1 = a
    x2, y2 = b
    return (x1-x2)**2 + (y1-y2)**2

for i in choice:
    ls = []
    p1 = pone[i[0]]
    p2 = pone[i[1]]
    p3 = pone[i[2]]
    p4 = pone[i[3]]
    ls.append(cal(p1,p2))
    ls.append(cal(p1,p3))
    ls.append(cal(p1,p4))
    ls.append(cal(p2,p3))
    ls.append(cal(p2,p4))
    ls.append(cal(p3,p4))
    ls.sort()
    x = ls[0]
    if ls[1]//x == 1 and ls[2]//x == 1 and ls[3]//x == 1 and ls[4]//x == 2 and ls[5]//x == 2:
        ans += 1

print(ans)