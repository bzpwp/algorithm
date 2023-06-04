n,m = map(int,input().split())
ls = []
for i in range(m):
    l = list(map(int,input().split()))
    l = l[1:]
    ls.append(l)
pl = list(map(int,input().split()))
A = 0
for i in range(2**n):
    on = set([])
    for j in range(n):
        if (i>>j)&1:
            on.add(j+1)
    # if i == 3:
        # print(on)
    num_on = 0
    for j in range(m):
        # if i == 3:
        #     print(set(ls[j]),j)
        if len(set(ls[j])&on)%2!=pl[j]:
            break
    else:
        A += 1
print(A)
