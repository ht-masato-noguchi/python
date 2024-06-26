import random

# ランダムな数を生成する
secret_number = random.randint(1, 100)
guess = None
attempts = 0

print("1から100までの数を当ててください!")

# ユーザーが数を当てるまでループを実行する
while guess != secret_number:
    guess = int(input("あなたの予想: "))
    attempts += 1
    
    if guess < secret_number:
        print("もっと大きい数です。")
    elif guess > secret_number:
        print("もっと小さい数です。")
    else:
        print(f"正解です! あなたは {attempts} 回で当てました。")


