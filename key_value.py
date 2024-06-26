# 変数宣言
test_score = {"math":"90", "japanese":"78", "english":"84"}

# 出力
print(test_score)

for dict_key in test_score:
    print("変数dict_keyに格納されている値：", dict_key)
    print("test_score[", dict_key, "]：", test_score[dict_key])