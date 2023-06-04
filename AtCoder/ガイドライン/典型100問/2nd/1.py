n,x = map(int,input().split())
import itertools

c = list(itertools.combinations(list(range(1,n+1)),3))
A = 0
for i in c:
    # print(i)
    # print(sum(i))
    if sum(i)==x:
        A +=1
print(A)