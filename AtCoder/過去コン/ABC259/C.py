s = input()
t = input()

ls = len(s)
lt = len(t)
j = 0
i = 0
while i <= ls-1:
    if i == ls-1:
        if j != lt-1:
            print("No")
            exit()
        elif s[-1]==t[-1]:
            print("Yes")
            exit()
        else:
            print("No")
            exit()
    elif s[i]==t[j] and s[i] == s[i+1]:
        if j == lt-1:
            print("No")
            exit()
        elif t[j] != t[j+1]:
            print("No")
            exit()
        else:
            i1 = 1
            j1 = 1
            while s[i]==s[i+i1]:
                i1 += 1
            while t[j]==t[j+j1]:
                j1 += 1
            if i1 > j1:
                print("No")
                exit()
            else:
                i += i1
                j += j1
    elif s[i]==t[j]:
        i += 1
        j += 1
    else:
        print("No")
        exit()
    
print("Yes")
            
