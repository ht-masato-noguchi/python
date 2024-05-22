# 単語を入力してリストに格納する
words = []
while True:
    word = input("単語を入力してください（終了するにはEnterキーを押してください）: ")
    if word:
        words.append(word)
    else:
        break

# 単語をアルファベット順に並び替えて表示する
if words:
    sorted_words = sorted(words)
    print("入力した単語をアルファベット順に並び替えると:")
    for word in sorted_words:
        print(word)
else:
    print("単語が入力されていません。")
