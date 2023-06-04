n = int(input().split())
l = []
for i in range(2*n-1):
    l.append(list(map(int,input().split())))
import itertools
x = list(itertools.permutations(range(1,n+1)))
