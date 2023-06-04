n,m = map(int,input().split())
lsab = [] 
lsc = [] 
for i in range(m): 
	lsab.append(list(map(int,input().split())))
for i in range(m): 
	lsc.append(list(map(int,input().split())))
import itertools
arr = list(range(1,n+1))
p = list(itertools.permutations(arr))
for l in p:
    x = 1
    for a in lsab:
        if [l[a[0]-1],l[a[1]-1]] not in lsc and [l[a[1]-1],l[a[0]-1]] not in lsc:
            x = x*0
    if x ==1:
        print("Yes")
        break
if x == 0:
    print("No")