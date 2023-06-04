n = int(input())
ls = list(map(int,input().split()))

ls.sort()

print(sum(ls[n:-n])/(3*n))