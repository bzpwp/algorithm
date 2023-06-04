n, x = map(int,input().split())
ls = [int(input()) for _ in range(n)]
print(int((x-sum(ls))/min(ls))+n)