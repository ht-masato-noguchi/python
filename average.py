# 数字を入力してリストに格納する
numbers = []
while True:
    try:
        num = float(input("数字を入力してください（終了するにはEnterキーを押してください）: "))
        numbers.append(num)
    except ValueError:
        break

# 平均を計算する
if numbers:
    average = sum(numbers) / len(numbers)
    print(f"入力した数字の平均値は {average} です。")
else:
    print("数字が入力されていません。")
