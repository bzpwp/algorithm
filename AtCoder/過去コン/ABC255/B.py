n,k = map(int, input().split())
lsa = list(map(int, input().split()))

import math

ls = [] 
for i in range(n): 
	ls.append(list(map(int,input().split())))

lsx = 0
for i in range(n):
    x = 10**18
    if i+1 not in lsa:
        for j in lsa:
            # print(i,j)
            # print(math.sqrt((ls[j-1][0]-ls[i][0])**2+(ls[j-1][1]-ls[i][1])**2))
            x = min(x,math.sqrt((ls[j-1][0]-ls[i][0])**2+(ls[j-1][1]-ls[i][1])**2))
        lsx = max(lsx,x)

print(lsx)