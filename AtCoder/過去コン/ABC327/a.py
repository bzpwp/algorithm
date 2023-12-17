n = int(input())
s = input()

for i in range(n-1):
    if s[i]=="a" and s[i+1]=="b":
        print("Yes")
        exit()
    elif s[i]=="b" and s[i+1]=="a":
        print("Yes")
        exit()
print("No")