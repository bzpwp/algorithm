n = int(input())  
ls = [int(input()) for _ in range(n)]
total = []
for i in range(max(ls)+1):
    if i in ls:
        total.append(i)
print(len(total))