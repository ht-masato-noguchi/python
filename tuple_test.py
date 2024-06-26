# 変数宣言
tuple_test = ("一個目", "二個目", "三個目", "四個目") #tupleは中のデータを操作できない
len_tuple_list = len(tuple_test)
count = 0

tuple_test[1] = "にこめ"

# 出力
while count < len_tuple_list:
    print("tuple_test[", count, "]：", tuple_test[count])
    
    count = count + 1