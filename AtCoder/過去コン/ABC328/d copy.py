s = input()

decide = []
kari = []

while len(s):
    if len(s)>=3 and s[0:3] == "ABC":
        s = s[3:]
    else:
        if len(s)>=2 and s[0:2] == "AB":
            kari.append("AB")
            s = s[2:]
        else:
            if s[0] == "A":
                kari.append("A")
                s = s[1:]
            else:
                if len(s)>=2 and s[0:2] == "BC":
                    if len(kari) and kari[-1] == "A":
                        kari.pop()
                    else:
                        decide += kari
                        decide.append("BC")
                        kari = []
                    s = s[2:]
                elif s[0] == "C":
                    if len(kari) and kari[-1] == "AB":
                        kari.pop()
                    else:
                        decide += kari
                        decide.append("C")
                        kari = []
                    s = s[1:]
                else:
                    decide += kari
                    decide.append(s[0])
                    kari = []
                    s = s[1:]

decide += kari
print("".join(decide))