n,p,q,r  = map(int, input().split())
ls = list(map(int, input().split()))

x = 0
ans = ls[0]
y = 1

# def kettei(a,b,c,d):
#     if a > b:
#         a -= ls[c]
#         c += 1
#     elif a < b:
#         a += ls[d]
#         d += 1
#     elif a == b:
#         return (a,c,d)
# try:
#     ans,x,y = kettei(ans,p,x,y)
# except:
#     print("No")
#     exit()

# z = y + 1


while True:
    # if x > n-3 or y > n-2 or z > n-1 or w > n:
    #     print("No")
    try:
        if ans > p:
            ans -= ls[x]
            x += 1
        elif ans < p:
            ans += ls[y]
            y += 1
        elif ans == p:
            z = y + 1
            ans2 = ls[z]
            if ans2 > q:
                ans2 -= ls[y]
                ans += ls[y]
                y += 1
                

    
    except:
        print("No")
        exit()

print("Yes")