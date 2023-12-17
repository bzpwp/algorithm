ls = ["A","B","C","D","E"]
s = input()
t = input()
ind = ls.index(s[0])
ind2 = ls.index(s[1])
x = abs(ind-ind2)
x = min(5-x,x)

ind3 = ls.index(t[0])
ind4 = ls.index(t[1])
y = abs(ind3-ind4)
y = min(5-y,y)

if x == y:
    print("Yes")
else:
    print("No")