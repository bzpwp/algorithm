n, w = map(int, input().split())
list_ = []
for _ in range(n):
    list_.append(list(map(int, input().split())))

list_.sort(reverse=True)
oisisa = 0
for i in range(n):
    a, b = list_[i]
    if w == 0:
        break
    elif w >= b:
        oisisa += a * b
        w -= b
    else:
        oisisa += a * w
        w = 0
print(oisisa)