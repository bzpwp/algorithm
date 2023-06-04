s = input()
t = input()

n = len(t)
diff = set([])
place = set([])
for i in range(n):
    if t[i]!= "?" and s[-n+i]!= "?" and t[i]!= s[-n+i]:
        diff.add(i)
    if t[i]== "?":
        place.add(i)

if diff == set([]):
    print("Yes")
else:
    print("No")

# print(place)
x = False

for j in range(n):
    if x:
        print("No")
    else:
        diff.discard(j)
        if j not in place and s[j]!= "?" and t[j]!= s[j]:
            x = True
            print("No")
        else:
            if diff == set([]):
                print("Yes")
            else:
                print("No")