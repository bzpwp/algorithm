n = int(input())

def d(a):
    return a//100, (a-(a//100)*100)//10, a%10

for i in range(n,920):
    a,b,c = d(i)
    if a*b == c:
        print(i)
        exit()