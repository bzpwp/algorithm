n = int(input())
s = input()

level = 0

ls = s.split("-")
if len(ls) == 1: #団子のみ
    # print(ls)
    print(-1)
else:
    for i in ls:
        level = max(level, len(i))
    if level == 0:
        print(-1)
    else:
        print(level)