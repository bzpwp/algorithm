s = input()
while True:
    if s[len(s)-6:len(s)-1] == "dream" or s[len(s)-6:len(s)-1] == "erase":
        s = s[:len(s)-5]
    if s[len(s)-7:len(s)-1] == "eraser":
        s = s[:len(s)-6]
    if s[len(s)-8:len(s)-1] == "dreamer":
        s = s[:len(s)-7]
    if s =="":
        print("YES")
        sys.exit()
    break
    else:
        print("NO")
        sys.exit()