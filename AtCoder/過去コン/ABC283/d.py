from collections import deque, defaultdict
s = deque(list(input()))
n = len(s)

box = set()
checkdic = defaultdict(list)
numleft = 0

for i in range(n):
    x = s.popleft()
    if x == "(":
        numleft += 1
    elif x == ")":
        for c in checkdic[numleft]:
            box.remove(c)
        checkdic[numleft] = []
        numleft -= 1
    else:
        if x in box:
            print("No")
            exit()
        else:
            box.add(x)
            checkdic[numleft].append(x)


    # print(checkdic,s,numleft)
    # print(box)


print("Yes")