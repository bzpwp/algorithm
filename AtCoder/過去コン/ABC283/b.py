n = int(input())
ls = list(map(int,input().split()))
q = int(input())

for i in range(q):
    j, *arg = input().split()
    if j == "1":
        k,x = arg
        ls[int(k)-1] = int(x)
    else:
        k = int(arg[0])
        print(ls[k-1])