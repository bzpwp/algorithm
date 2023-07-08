n = int(input())
ls = []
for i in range(n):
    a,b = map(int,input().split())
    ls.append(a/(a+b))
xz = sorted(range(len(ls)),key=ls.__getitem__,reverse=True)
xz = [i+1 for i in xz]
print(*xz)