ls = list(map(int,input().split()))

for i in range(8):
    if i!=0:
        if ls[i-1] > ls[i]:
            print("No")
            exit()
    if ls[i] < 100 or ls[i] > 675:
        print("No")
        exit()
    if ls[i]%25 != 0:
        print("No")
        exit()
print("Yes")