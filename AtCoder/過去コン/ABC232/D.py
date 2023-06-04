import itertools
h,w = map(int,input().split())
ls = [] 
for i in range(h): 
	ls.append(input())
a = (h-1)*[0]
a += (w-1)*[1]
import itertools
ls1 = list(set(list(itertools.permutations(a))))
b = []
for l in ls1:
    x = 1
    y = 1
    z = 0
    for i in (l):
        if i==1:
            x += 1
        else:
            y += 1
        if ls[y-1][x-1] == ".":
            z += 1
        else:
            break
    b.append(z)
print(max(b)+1)