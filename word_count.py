# 単語のカウントをするプログラム
text = input("任意のテキストを入力してください: ")

# テキストをスペースで分割して単語のリストを作成する
words = text.split()

# 単語数をカウントする
word_count = len(words)

# 結果を表示する
print(f"入力されたテキストには {word_count} 単語が含まれています。")

