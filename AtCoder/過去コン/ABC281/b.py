s = input()

wls = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

if s[0] in wls:
    if s[-1] in wls:
        try:
            if 100000 <= int(s[1:-1]) <= 999999:
                print("Yes")
            else:
                print("No")
        except:
            print("No")
        exit()

print("No")