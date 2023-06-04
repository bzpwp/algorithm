n = int(input())
ls = [] 
for i in range(n): 
	ls.append(str(input()))

import sys
sys.setrecursionlimit(10**6)

l = []
def func(a,b,c,d):
    if d[b%n][c%n]==".":
        if len(a)==4:
            l.append(int(a))
        else:
            d[b%n][c%n]="#"
            a += str(ls[b%n][c%n])
            func(a,b+1,c+1,d)
            func(a,b,c+1,d)
            func(a,b+1,c,d)
            func(a,b+1,c-1,d)
            func(a,b-1,c-1,d)
            func(a,b,c-1,d)
            func(a,b-1,c,d)
            func(a,b-1,c+1,d)
    else:
        func(a,b+1,c+1,d)
        func(a,b,c+1,d)
        func(a,b+1,c,d)
        func(a,b+1,c-1,d)
        func(a,b-1,c-1,d)
        func(a,b,c-1,d)
        func(a,b-1,c,d)
        func(a,b-1,c+1,d)
        

x = 0
for i in range(n):
    for j in range(n):
        check = [["."]*n]*n
        func("",i,j,check)

print(max(l))