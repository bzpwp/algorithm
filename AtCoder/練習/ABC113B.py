n = int(input())
t, a = map(int, input().split())
ls = list(map(int, input().split()))
te = []
for i in ls:
    te += [t-0.006*i-a]
so = [abs(x) for x in te]
print(so.index(min(so))+1)
