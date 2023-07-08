n = int(input())
s = input()

from collections import deque

s_all = deque([])
for i in s:
    s_all.append(i)
new_s = deque([])
index = deque([])

ind = 0
while s_all:
    ind += 1
    c = s_all.popleft()
    new_s.append(c)
    if c == "(":
        index.append(ind)
    elif c == ")":
        if index:
            num = index.pop()
            # print(num,ind)
            for i in range(ind-num+1):
                new_s.pop()
                ind = num - 1
        else:
            pass
    else:
        pass
    # print(new_s)


print("".join(list(new_s)))
