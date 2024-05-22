# 数字を入力してリストに格納する
numbers = []
while True:
    try:
        num = float(input("数字を入力してください（終了するにはEnterキーを押してください）: "))
        numbers.append(num)
    except ValueError:
        break

# 数字を昇順に並び替えて表示する
if numbers:
    sorted_numbers = sorted(numbers)
    print("入力した数字を昇順に並び替えると:")
    for num in sorted_numbers:
        print(num)
else:
    print("数字が入力されていません。")

