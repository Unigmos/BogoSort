import random

#ソートする配列とカウンター初期値の設定
a = [3, 5, 2, 1, 4]
counter = 0

#メイン処理
while True:
    if a == sorted(a):
        break
    random.shuffle(a)
    counter += 1
    print(a)
    
print(f"試行回数{counter}回")
