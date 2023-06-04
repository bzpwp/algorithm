n = int(input())
ls = [input() for _ in range(n)]
dic = {}
for i in range(n):
    dic[ls[i]] = ls.count(ls[i])
max_k = max(dic, key=dic.get)
print(max_k)