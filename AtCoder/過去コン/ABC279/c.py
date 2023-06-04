h, w  = map(int, input().split())
sgrid = ["" for _ in range(w)]
tgrid = ["" for _ in range(w)]

for i in range(h):
    s = input()
    for j in range(w):
        sgrid[j] += s[j]
    
for i in range(h):
    t = input()
    for j in range(w):
        tgrid[j] += t[j]

# from collections import Counter
# dds = Counter(sgrid)
# ddt = Counter(tgrid)

dds = sgrid.sort()
ddt = tgrid.sort()
print(sgrid)
print(tgrid)
if dds == ddt:
    print("Yes")
else:
    print("No")

