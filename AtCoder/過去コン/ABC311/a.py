n = int(input())
s = input()
l = set([])

for i in range(n):
    l.add(s[i])
    if l == set(["A","B","C"]):
        print(i+1)
        exit()