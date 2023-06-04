s = input()
t = input()
sls= []
tls = []
wls = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
nls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
for c in s:
    sls.append(nls[wls.index(c)])
for c in t:
    tls.append(nls[wls.index(c)])
x = 1
y = sls[0]- tls[0]
if y > 0: 
    y -= 26
for i in range(1,len(s)):
    z = sls[i]- tls[i]
    if z > 0:
        z -= 26
    if z != y:
        x = 0
if x == 1:
    print("Yes")
else:
    print("No")