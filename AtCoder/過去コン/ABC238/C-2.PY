n = int(input())
l = len(str(n)) #桁数
x = 0
def func1(a):
    if a == 
        return 
    a -= 1
    func1(a)+sum(range(10(a), 9*10(a)))
def func2(b):
    return func2(b-1)+func1(b)
print(func2(l))