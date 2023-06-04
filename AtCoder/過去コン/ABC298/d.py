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
        digit += 1

    elif que == "2":
        s %= 10**(digit-1)
    else:
        # print("^^^")
        print(s%M)