s = input()

if s[0]==s[1] and s[1]==s[2]:
    print(-1)
    exit()

wls = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ls = []
for i in s:
    if i in wls:
        ls.append(i)

print(ls)
ls2 = []
for i in range(2):
    for j in range(i+1,3):
        if ls[i]==ls[j]:
            ls2.append(ls[i])


for i in ls:
    if i not in ls2:
        print(i)
        exit()