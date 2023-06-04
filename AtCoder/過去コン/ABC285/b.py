n = int(input())

s = input()

for i in range(n-1):
    # a = 0
    for k in range(n-i-1):
        if k == n-i-2:
            if s[k] != s[k+i+1]:
                # print("c")
                print(k+1)
            else:
                # print("b")
                print(k)
        # print("--",k)
        elif s[k] == s[k+i+1]:
            # print("a")
            print(k)
            break

