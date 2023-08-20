n = int(input())
ls = list(map(int,input().split()))

if n == 1:
    print(0)
else:
    x = ls[0]
    ls = ls[1:]
    if x > max(ls):
        print(0)
    else:
        print(max(ls) - x + 1)