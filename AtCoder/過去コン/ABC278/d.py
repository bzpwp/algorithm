n = int(input())
ls = list(map(int,input().split()))

q = int(input())

for i in range(q):
    a, *b = input().split()
    a = int(a)
    if a == 1:
        ls = [int(*b)]*n
    elif a == 2:
        ls[int(b[0])-1] += int(b[1])
    else:
        print(ls[int(*b)-1]) 