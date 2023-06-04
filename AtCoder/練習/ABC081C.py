n,k = map(int, input().split())
ls = list(map(int, input().split()))
dic = {}
x = 0
for value in ls:
    dic[value]=ls.count(value)
ls1 = list(dic.values())
ls1.sort()
if len(dic)<=k:
    print(0)
else:
    print(sum(ls1[:len(ls1)-k]))