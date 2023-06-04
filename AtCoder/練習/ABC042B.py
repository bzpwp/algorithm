n,l = map(int,input().split())
ls = [input() for _ in range(n)]
ls.sort()
print(''.join(ls))