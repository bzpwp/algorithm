n = int(input())

wls = []

ls = []
for i in range(n):
    s = input()
    ls.append(s)
    wls.append(s[0])

x = 0
for i in range(n):
    for j in ls:
        if j[-1] not in wls:
            if x % 2 ==0:
                print("First")
            else:
                print("Second")
        else:
            