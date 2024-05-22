# 数字を入力してリストに格納する
numbers = []
while True:
    try:
        num = int(input("数字を入力してください（終了するには0を入力してください）: "))
        if num == 0:
            break
        numbers.append(num)
    except ValueError:
        print("有効な数字を入力してください。")

# 偶数だけを抽出して表示する
if numbers:
    even_numbers = [num for num in numbers if num % 2 == 0]
    if even_numbers:
        print("入力した数字の中で偶数は以下の通りです:")
        for num in even_numbers:
            print(num)
    else:
        print("偶数は入力されていません。")
else:
    print("数字が入力されていません。")
