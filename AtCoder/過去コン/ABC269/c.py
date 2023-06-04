n = int(input())

import copy

num_2 = bin(n)[2:]
digit = len(num_2)
ls=[]
for i in range(digit):
    if num_2[i]=="1":
        ls.append(i)
ls.sort(reverse=True)

num_3 = len(ls)

for i in range(2**num_3):
    s = ["0"]*digit
    for j in range(num_3):
        if i>>j & 1:
            s[ls[j]]="1"
    print(int("".join(s),2))