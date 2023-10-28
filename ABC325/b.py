n = int(input())
ls = [0 for i in range(24)]
for i in range(n):
    w,x = map(int,input().split())
    for j in range(9-x, 18-x):
        ls[j] += w
print(max(ls))