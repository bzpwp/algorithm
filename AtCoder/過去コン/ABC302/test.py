from collections import defaultdict

# defaultdictを作成
my_dict = defaultdict(int)
my_dict['key1'] = 1
my_dict['key2'] = 2
my_dict['key3'] = 3

# 特定の要素を削除
del my_dict['key2']

# 削除後の辞書の内容を表示
print(my_dict)
