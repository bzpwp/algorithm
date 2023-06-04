s = input()

wls = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

if len(s)!=8:
    # print("c")
    print("No")
    exit()

if s[-1] not in wls:
    # print("b")
    print("No")
    exit()

if s[0] not in wls:
    # print("a")
    print("No")
    exit()

try:
    x = int(s[1:-1])
    if 100000 <= x <= 999999:
        print("Yes")
    else:
        print("No")

except:
    print("No")