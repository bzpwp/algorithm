n = hex(int(input()))[2:].replace("a","A").replace("b","B").replace("c","C").replace("d","D").replace("e","E").replace("f","F")

if len(n)==2:
    print(n)
else:
    print("0"+n)