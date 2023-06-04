s = list(input())
t = list(input())

from collections import Counter

cs = Counter(s)
ct = Counter(t)

check = set(["a","t","c","o","d","e","r"])
# check = ["a","t","c","o","d","e","r"]

wls = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
s_to_t = 0
t_to_s = 0
for i in wls:
    if cs[i]!=ct[i]:
        if i not in check:
            print("No")
            exit()
        else:
            if cs[i]>ct[i]:
                t_to_s += cs[i]-ct[i]
            else:
                s_to_t += ct[i]-cs[i]
if cs["@"] >= s_to_t and ct["@"] >= t_to_s:
    print("Yes")
    exit()
print("No")