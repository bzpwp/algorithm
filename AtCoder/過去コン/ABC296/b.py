x = ["a","b","c","d","e","f","g","h"]
for i in range(8):
    s = input()
    for j in range(8):
        if s[j] == "*":
            print(x[j]+str(8-i))