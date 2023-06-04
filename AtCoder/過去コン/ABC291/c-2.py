n = int(input())
s = input()

from collections import defaultdict
dd = defaultdict(set)
x,y = [0,0]
dd[x].add(y)

for i in s:
    if i == "R":
        x += 1
        if y in dd[x]:
            print('Yes')
            exit()
        dd[x].add(y)
    elif i =="L":
        x -= 1
        if y in dd[x]:
            print('Yes')
            exit()
        dd[x].add(y)
    elif i =="U":
        y += 1
        if y in dd[x]:
            print('Yes')
            exit()
        dd[x].add(y)
    elif i =="D":
        y -= 1
        if y in dd[x]:
            print('Yes')
            exit()
        dd[x].add(y)

print("No")
