n = int(input())
ls = set([])
for i in range(n):
    s = input()
    if s in ls:
        print("No")
        exit()
    else:
        ls.add(s)
        if s[0]!= "H" and s[0]!= "D" and s[0]!= "C" and s[0]!= "S":
            print("No")
            exit()
        else:
            if s[1]!="A" and s[1]!="2" and s[1]!="3" and s[1]!="4" and s[1]!="5" and s[1]!="6" and s[1]!="7" and s[1]!="8" and s[1]!="9" and s[1]!="T" and s[1]!="J" and s[1]!="Q" and s[1]!="K":
                print("No")
                exit()

print("Yes")