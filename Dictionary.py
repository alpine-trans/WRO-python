# 辞書
# 配列の亜種みたいなやつ
# 辞書名 = {キー1：値1, キー2：値2, ...}
# キー(key)と値を対応させる。キーには変更不可能なデータを入れる(文字列，数値，タプル 等)。同じ辞書の中では、同じ値のキーは使えない。


# 例 家族の年齢についての辞書

# 辞書を定義
family_ages = {'son' : 14, 'mother' : 43, 'father' : 45}
print(family_ages)   # ⇒ {'son' : 14, 'mother' : 43, 'father' : 45}

# キーに対応する値を取得
print(family_ages['son'])   # ⇒ 14

# 値を変更するには
family_ages['mother'] = 44

# 新しいキーと値を登録するには
family_ages['brother'] = 18
print(family_ages)   # ⇒ {'son' : 14, 'mother' : 44, 'father' : 45, 'brother' : 18}

# そのキーが存在するか調べるには
if 'father' in family_ages:
  print(True)
else:
  print(False)
# ⇒ True
if 'sister' in family_ages:
  print(True)
else:
  print(False)
# ⇒ False

# len() 辞書のキーと値のペアの数を調べるには
print(len(family_ages))   # ⇒ 4

# del 特定のキーを削除するには
del family_ages['father']
print(family_ages)   # ⇒ {'son' : 14, 'mother' : 44, 'brother' : 18}

# メソッド編
# .keys() キーの一覧を取得する
print(family_ages.keys())   # ⇒ dict_keys(['son','mother','brother'])
# for文と組み合わせると
for key in family_ages.keys():
  print(key)
# ⇒ son
#    mother
#    brother
# List型と組み合わせると
print(list(family_ages.keys()))   # ⇒ ['son','mother','brother']

# .values() 値の一覧を取得する
print(family_ages.values())   # ⇒ dict_values([14,44,18])
# for文と組み合わせると
for value in family_ages.values():
  print(value)
# ⇒ 14
#    44
#    18
#List型と組み合わせると
print(list(family_ages.values()))   # ⇒ [14,44,18]

# .items() キーと値の組み合わせの一覧を取得する
print(family_ages.items())   # ⇒ dict_items([('son',14),('mother',44),('brother',18)])
# for文と組み合わせると
for key,value in family_ages.items():
  print("key:"+key + ", value:"+value)
# ⇒ key:son, value:14
#    key:mother, value:44
#    key:brother, value:18
# List型と組み合わせると
print(list(family_ages.items()))   # ⇒ [('son',14),('mother',44),('brother',18)]

# .get(key,なかった場合の値) 特定のキーの値を取得する
print(family_ages.get('brother','UNKNOWN'))   # ⇒ 18
print(family_ages.get('sister','UNKNOWN'))   # ⇒ UNKNOWN

# .pop(key,なかった場合の値) 特定のキーの値を取得し、それを削除する
print(family_ages.pop('mother','UNKNOWN'))   # ⇒ 44
print(family_ages.pop('father','UNKNOWN'))   # ⇒ UNKNOWN
print(family_ages)   # ⇒ {'son' : 14, 'brother' : 18}

# .update(dictionary) 別の辞書を結合させる
parents_ages =  {'mother' : 44, 'father' : 45}
family_ages.update(parents_ages)
print(family_ages)  # ⇒ {'son' : 14, 'brother' : 18, 'mother' : 44, 'father' : 45}

# .copy(dictionary) 辞書を複製する
new_family_ages = family_ages.copy()
print(new_family_ages)  # ⇒ {'son' : 14, 'brother' : 18, 'mother' : 44, 'father' : 45}

# .clear() 辞書の中身を削除する
new_family_ages.clear()
print(new_family_ages)  # ⇒ {}

# .setdefault(key.なかった場合の値) 特定のキーの値を取得し、それが存在しない場合、そのキーと値を追加する
print(family_ages.setdefault('son',''))   # ⇒ 14
print(family_ages.setdefault('sister','16'))   # ⇒ 16
print(new_family_ages)  # ⇒ {'son' : 14, 'brother' : 18, 'mother' : 44, 'father' : 45, 'sister' : 16}

# dict.fromkeys(keys,values) 特定のリストから辞書を作成する
twins_keys = ['elder','younger']
twins_value = 15
twins_ages = dict.fromkeys(twins_keys, twins_value)
print(twins_ages)   # ⇒ {'elder' : 15, 'younger' : 15}
brothers_keys = ['elder','younger']
brothers_values = [19,15]
brothers_ages = dict.fromkeys(brothers_keys, brothers_values)
print(brothers_ages)   # ⇒ {'elder' : 19, 'younger' : 15}

# .popitem() ランダムなキーと値の組み合わせを取得し、削除する
key,value = family_ages.popitem()
print(key,item)   # ⇒ 'son',14
print(family_ages)  # ⇒ {'brother' : 18, 'mother' : 44, 'father' : 45}
