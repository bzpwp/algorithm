n = int(input())
ls = []
# lsr = []
for i in range(n):
    s = input()
    ls.append(s)
    # lsr.append(s[::-1])

# for i in range(n-1):
#     for j in range(i+1,n):
#         if ls[i] == lsr[j]:
#             print("Yes")
#             exit()
# print("No")
# print(ls)

x  = 0
for i in range(n-1):
    for j in range(i+1,n):
        x += 1
        ns = ls[i]+ls[j]
        ns2 = ls[j]+ls[i]
        if ns == ns[::-1]:
            print("Yes")
            exit()
        elif ns2 == ns2[::-1]:
            print("Yes")
            exit()
print("No")