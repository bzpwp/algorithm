#  リストの要素の個数を調べる
import collections  #  collectionsライブラリのインポートが必須です。
list = ['a', 'b', 'c', 'a', 'b', 'b']
clist = collections.Counter(list)
print(clist)
print(clist["a"])
clist["d"]+=1
print(clist)