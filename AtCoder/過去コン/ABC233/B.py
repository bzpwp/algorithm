l,r = map(int,input().split())
s = input()
if l ==1:
    x1 = ""
else:
    x1 =  s[:l-1]
if r == len(s):
    x3 =""
else:
    x3 = s[r:]
x2 = s[l-1:r]
new_x2 = ''.join(list(reversed(x2)))
print(x1+new_x2+x3)