n = int(input())
ls = list(map(int,input().split()))
a = 0
b = 0
while ls != []:
    a += max(ls)
    ls.remove(max(ls))
    if ls != []:
        b += max(ls)
        ls.remove(max(ls))
print(a-b)