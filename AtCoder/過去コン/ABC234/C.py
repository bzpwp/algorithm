k = int(input())
x = k
y = 1 #桁数
while x >1:
    x = x//2
    y += 1 #桁数
z = k - 2**(y-1) #sその中で何番目か
if z == 0:
    print(int(str(2)+str(0)*(y-1)))
if z == 1:
    print(int(str(2)+str(0)*(y-2)+str(2)))
else:
    a = "" #ここに追加
    while z >1:
        if z % 2 ==1:
            a += "1"
        else:
            a += "0"
        z = z//2
    a += "1"
    a = a[::-1]
    a += "0"*((y-1)-len(a))
    a.replace('1', '2')
    print(int(str(2)+a))