n,p,q = map(int,input().split())
ls = list(map(int,input().split()))

print(min(p,q+min(ls)))