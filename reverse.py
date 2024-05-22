# 文字列を入力してリストに格納する
strings = []
while True:
    string = input("文字列を入力してください（終了するにはEnterキーを押してください）: ")
    if string:
        strings.append(string)
    else:
        break

# 入力した文字列を逆順にして表示する
if strings:
    print("入力した文字列を逆順にすると:")
    for string in strings:
        print(string[::-1])
else:
    print("文字列が入力されていません。")

