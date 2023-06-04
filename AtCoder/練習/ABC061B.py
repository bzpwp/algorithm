n,m = map(int,input().split())
ls = [] 
for i in range(m): 
	ls.append(list(map(int,input().split())))

ls1 = []
x = 0
for a in range(n):
    for b in range(m):
        if ls[b][0] == a+1:
            x +=1
        if ls[b][1] == a+1:
            x +=1
    ls1.append(x)
    x = 0
for value in ls1:
    print(value)
