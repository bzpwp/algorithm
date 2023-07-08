n = int(input())
ls = list(map(int,input().split()))
for i in range(n):
    # print(n*i)
    # print((i+1)*n)
    print(sum(ls[7*i:(i+1)*7]))