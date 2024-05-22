# 数字を入力してリストに格納する
numbers = []
while True:
    try:
        num = float(input("数字を入力してください（終了するにはEnterキーを押してください）: "))
        numbers.append(num)
    except ValueError:
        break

# 最大値と最小値を見つける
if numbers:
    max_num = max(numbers)
    min_num = min(numbers)
    print(f"入力した数字の中で最大値は {max_num} です。")
    print(f"入力した数字の中で最小値は {min_num} です。")
else:
    print("数字が入力されていません。")

