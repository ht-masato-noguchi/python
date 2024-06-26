# 変数宣言
station_list = ["新宿", "代々木", "原宿", "渋谷"]

# 停車駅の表示
for station in station_list:
    if station == "新宿":
        print("出発地点：", station)
    elif station == "渋谷":
        print("到着地点：", station)
    else:
        print("通過地点：", station)