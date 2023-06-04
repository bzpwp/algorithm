s = input()
def fact(x): #階乗関数
    if x == 0:
        return 1
    else:
        return x * fact(x - 1)
total = 0
for a in range(len(s)):
    for b in range(1,len(s)-a):
        total+=int(s[a:a+b])*sum(fact(len(s)-a-1)/(fact(i)*fact(len(s)-a-1-i)) for i in range(len(s)-a-1))
print(int(total))