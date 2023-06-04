a,b,c = input().split()
d,e,f = input().split()
if d == b and e == c and f == a:
    print("Yes")
elif d == c and e == a and f == b:
    print("Yes")
elif a == d and b == e and c == f:
    print("Yes")
else:
    print("No")