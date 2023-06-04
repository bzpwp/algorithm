n = int(input())
ls = [list(map(int,input().split())) for _ in range(n)]
import math
import itertools
c = list(itertools.permutations(list(range(n)),n))

sum = 0
for i in c:
    s = 0
    for j in range(n-1):
        s += math.sqrt((ls[i[j]][0]-ls[i[j+1]][0])**2+(ls[i[j]][1]-ls[i[j+1]][1])**2)
    sum += s
print(sum/len(c))