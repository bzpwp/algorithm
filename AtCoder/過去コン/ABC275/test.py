#逆元
M = 998244353
print(pow(3, -1, M))
#mod97における38の逆元
print(pow(2, -1, M))

print((pow(3, -1, M)*pow(2, -1, M))%M)
print(pow(1, -1, M)%M)
