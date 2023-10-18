n = int(input())

def check(s):
    x = 0
    for i in s:
        if i == "(":
            x += 1
        else:
            x -= 1
        if x < 0:
            return False
    return True


if n%2 == 1:
    print()
else:
# l = [0,1,2,3,4,5]
    import itertools
# ls = list(itertools.combinations(l,3))
# print(ls)
    l = [i for i in range(n)]
    ls = list(itertools.combinations(l,n//2))
    A = []
    for i in ls:
        x = ["("]*n
        # print(x)
        for j in i:
            # print(j)
            # print(x[j])
            x[j] = ")"
        if check(x):
            A.append("".join(x))
    A.sort()
    for i in A:
        print(i)
