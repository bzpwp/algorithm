n = int(input())
ls = []
x = 10**100000
ind = 1000
for i in range(n):
    s,a = input().split()
    if int(a) < x:
        x = int(a)
        ind = i
    ls.append(s)
# print(ind)
x = ls[ind:] + ls[:ind]
for i in x:
    print(i)