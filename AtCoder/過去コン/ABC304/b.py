n = input()

if len(n)<=3:
    print(int(n))
else:
    x = len(n)-3
    # print(x)
    print(int(n[:3] + "0"*x))