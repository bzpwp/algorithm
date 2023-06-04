h,w  = map(int, input().split())

ls = [] 
for i in range(h): 
	ls.append(list(input()))


def move(x,y):
    # print(x,y)
    print(ls)
    if ls[x][y]==".":
        print(-1)
        exit()

    elif ls[x][y]=="U":
        if x == 0:
            print(x+1,y+1)
            exit()
        else:
            ls[x][y]="."
            move(x-1,y)

    elif ls[x][y]=="D":
        if x == h-1:
            print(x+1,y+1)
            exit()
        else:
            ls[x][y]="."
            move(x+1,y)

    elif ls[x][y]=="L":
        if y == 0:
            print(x+1,y+1)
            exit()
        else:
            ls[x][y]="."
            move(x,y-1)

    elif ls[x][y]=="R":
        if y == w-1:
            print(x+1,y+1)
            exit()
        else:
            ls[x][y]="."
            move(x,y+1)
    
move(0,0)