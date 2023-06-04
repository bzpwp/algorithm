from typing import no_type_check

n = int(input()) 
ls = [] 
for i in range(n): 
	ls.append(list(map(int,input().split())))
ls0 = []
ls1 = []
for i in range(n):
    if ls[i][2]==0:
        ls0.appned(ls[i])
    else:
        ls1.append(ls[i])
len1 = len(ls1)
len0 = len(ls0)
for x in range(101):
    for y in range(101):
        H = ls1[0][2]+abs(ls1[0][0]-x)+abs(ls1[0][1]-y)
        for i in range(1,len1):
            if H != ls1[i][2]+abs(ls1[i][0]-x)+abs(ls1[i][1]-y):
                break
        for i in range(1,len0):
            if H - (abs(ls1[i][0]-x)+abs(ls1[i][1]-y)) > 0:
                break
print(x,y,H)