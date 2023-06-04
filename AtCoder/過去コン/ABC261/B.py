n = int(input())
ls = [] 
for i in range(n): 
	ls.append(input())

def func(a,b):
    if ls[a][b]=="W":
        if ls[b][a]!="L":
            return True
        else:
            return False
    elif ls[a][b]=="D":
        if ls[b][a]!="D":
            return True
        else:
            return False
    elif ls[a][b]=="L":
        if ls[b][a]!="W":
            return True
        else:
            return False
    
for i in range(n-1):
    for j in range(i+1,n):
        # print(i,j)
        # print(ls)
        # print(ls[i][j])
        if func(i,j):
            print("incorrect")
            exit()
print("correct")