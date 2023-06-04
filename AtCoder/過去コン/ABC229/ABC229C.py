n,w = map(int, input().split())
ls = [list(map(int,input().split())) for i in range(n)]
o = [ls[i][0] for i in range(n)]
total = 0
x = 0 
while total < w:
    if o == []:
        break
    lastcheese = max(o)
    y = o.index(max(o))
    x += lastcheese*ls[y][1]
    total += ls[y][1]
    o.remove(max(o))
    ls.remove(ls[y])
if total > w:
    print(x-lastcheese*(total-w))
else:
    print(x)