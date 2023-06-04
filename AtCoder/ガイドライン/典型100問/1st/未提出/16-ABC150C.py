import itertools

n = int(input())
p = list(map(int,input().split()))
q = list(map(int,input().split()))

ls = list(itertools.permutations(list(range(1,n+1)),n))

for i in range(len(ls)):
    l = list(ls[i])
    if l == p:
        a = i
    if l == q:
        b = i

print(abs(a-b))