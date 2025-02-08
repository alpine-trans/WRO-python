# 辞書
# 配列の亜種みたいなやつ
# 辞書名 = {キー1：値1, キー2：値2, ...}
# キー(key)と値を対応させる。キーには変更不可能なデータを入れる(文字列，数値，タプル 等)。同じ辞書の中では、同じ値のキーは使えない。

# 例 家族の年齢についての辞書
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
# 辞書のキーと値のペアの数を調べるには
print(len(family_ages))   # ⇒ 4
# 特定のキーを削除するには
del family_ages['father']
print(family_ages)   # ⇒ {'son' : 14, 'mother' : 44, 'brother' : 18}



