n = int(input())

ls = [[1],[1,1]]
if n ==1:
    print(1)
elif n == 2:
    for l in ls:
        print(*l)
else:
    for a in range(n-2):
        nl = [1]
        for b in range(a+1):
            nl.append(ls[a+1][b]+ls[a+1][b+1])
        nl.append(1)
        ls.append(nl)

    for l in ls:
        print(*l)