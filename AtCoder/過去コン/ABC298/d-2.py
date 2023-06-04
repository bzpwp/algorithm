q = int(input())
M = 998244353
s = 1
digit = 1
for i in range(q):
    que, *x = input()
    if que == "1":
        x = int(x[1])
        s *= 10
        s += x
        s %= M
        digit += 1
        print("---",s)
    elif que == "2":
        s = s*pow(10**(len(str(s)-1)), -1, M)
        # s = s*pow(10**(digit-1), -1, M)
        # s %= 10**(len(str(s))-1)
        digit -= 1
    else:
        print("^^^")
        print(s%M)