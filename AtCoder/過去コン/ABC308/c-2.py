n = int(input())
ls = []
for i in range(n):
    a,b = map(int,input().split())
    ls.append(a/(a+b))
A = [i[0]+1 for i in sorted(enumerate(ls), key=lambda x:x[1], reverse=True)]


print(*A)
