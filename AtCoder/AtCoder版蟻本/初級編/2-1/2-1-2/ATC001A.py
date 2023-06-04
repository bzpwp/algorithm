h, w = map(int,input().split())

import sys
sys.setrecursionlimit(10**8)

ls = [] 
for i in range(h): 
	ls.append(input())


for a in range(h):
    for b in range(w):
        if ls[a][b]=="s":
            x1 = a
            y1 = b

print(x1,y1)

def func(x,y):
    if (0<=x and x<=h-1) and (0<=y and y<=w-1):
        print("中")
        if ls[x][y]=="g":
            print("ゴール")
            print("Yes")
            exit()
        elif ls[x][y]==".":
            func(x-1,y)
            func(x+1,y)
            func(x,y-1)
            func(x,y+1)
        elif ls[x][y]=="s”
            func(x-1,y)
            func(x+1,y)
            func(x,y-1)
            func(x,y+1)

func(x1,y1)


print("No")