s = input()


if s[0]!="0":
    print("No")
    exit()
else:
    if s[6]=="1":
        if s[3]=="0":
            if s[1]=="1" or s[7]=="1" or s[4]=="1" or s[2]=="1" or s[8]=="1" or s[5]=="1" or s[9]=="1":
                print("Yes")
                exit()
        else:
            if s[2] == "0" and s[7]=="0":
                if s[4]=="1" or s[2]=="1" or s[8]=="1" or s[5]=="1" or s[9]=="1":
                    print("Yes")
                    exit()
            else:
                if s[4]=="0":
                    if s[2]=="1" or s[8]=="1" or s[5]=="1" or s[9]=="1":
                        print("Yes")
                        exit()
                else:
                    if s[2]=="0" and s[8]=="0":
                        if s[5]=="1" or s[9]=="1":
                            print("Yes")
                            exit()
                    else:
                        if s[5]=="0":
                            if s[9]=="1":
                                print("Yes")
                                exit()
    else:
        if s[4]=="1":
            if s[1]=="0" and s[7]=="0":
                if s[4]=="1" or s[2]=="1" or s[8]=="1" or s[5]=="1" or s[9]=="1":
                    print("Yes")
                    exit()
            else:
                if s[4]=="0":
                    if s[2]=="1" or s[8]=="1" or s[5]=="1" or s[9]=="1":
                        print("Yes")
                        exit()
                else:
                    if s[2] == "0" and s[8]=="0":
                        if s[5] =="1" or s[9]=="1":
                            print("Yes")
                            exit()
                    else:
                        if s[5]=="0":
                            if s[9]=="1":
                                print("Yes")
                                exit()
        else:
            if s[1]=="1" or s[7]=="1":
                if s[4]=="0":
                    if s[2]=="1" or s[8]=="1" or s[5]=="1" or s[9]=="1":
                        print("Yes")
                        exit()
                else:
                    if s[2]=="0" and s[8]=="0":
                        if s[5]=="1" or s[9]=="1":
                            print("Yes")
                            exit()
                    else:
                        if s[5]=="0":
                            if s[9]=="1":
                                print("Yes")
                                exit()
            else:
                if s[4]=="1":
                    if s[2]=="0" and s[8]=="0":
                        if s[5]=="1" or s[9]=="1":
                            print("Yes")
                            exit()
                    else:
                        if s[5]=="0":
                            if s[9]=="1":
                                print("Yes")
                                exit()
                else:
                    if s[2] =="1" or s[8]=="1":
                        if s[5]=="0":
                            if s[9]=="0":
                                print("Yes")
                                exit()

print("No")
                                                
                    