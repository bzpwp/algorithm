n =[int(i) for i in list(input())]


for i in range(len(n)-1):
    if n[i] <= n[i+1]:
        print("No")
        exit()
print("Yes")