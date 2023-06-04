s = input()
c = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u' ,'v', 'w', 'x', 'y', 'z']
ls = []
for i in c:
    if i not in s:
        ls.append(i)
if ls == []:
    print("None")
else:
    print(ls[0])
