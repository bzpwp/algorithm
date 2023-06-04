n = int(input())
ls = list(input().split())
s = set(["and", "not", "that", "the", "you"])
for i in ls:
    if i in s:
        print("Yes")
        exit()
print("No")