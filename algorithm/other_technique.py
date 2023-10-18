'''
転置して総和
'''
# 入力
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

# 前処理
yoko = list(map(sum, A))
tate = list(map(sum, zip(*A)))

'''
回転させながらfor文
'''
a,b,c = map(int,input().split())
for i in range(3):
    # 何らかの操作
    a,b,c = b,c,a

'''
場所と値を紐づけてO(N)
'''
ls = [4,2,3,0,1]
dd = {ls[i]:i for i in range(5)}
# 毎回値の場所を探していたら時間がかかるのでこの辞書ですぐにインデックスを取得できる。

'''
permutationsでは1対1対応の場合、場所とインデックスを逆転させてもよい。(全探索の場合)
'''
import itertools
ls = list(itertools.permutations(list(range(5)),5))
# 例えば(4,2,3,0,1)となった時、0,1,2,3,4のインデックスがそれぞれ(4,2,3,0,1)と見做しても、4,2,3,0,1のインデックスがそれぞれ(0,1,2,3,4)であると見做しても良い。