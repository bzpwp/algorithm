n = int(input())
s = input()

s = set()
x,y = [0,0]
s.add([0,0])

for i in s:
    if s == "R":
        x += 1
        s.add([x,y])
    elif s =="L":
        x -= 1
        s.add([x,y])
    elif s =="U":
        x += 1
        s.add([x,y])
    elif s =="D":
        x -= 1
        s.add([x,y])
    
    print(s)
    if [x,y] in s:
        print("Yes")
        exit()

print("No")
