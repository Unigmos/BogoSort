import random

a = [3, 5, 2, 1, 4]
counter = 0

shuffle_data = random.shuffle(a)
counter += 1

while True:
    random.shuffle(a)
    counter += 1
    print(a)
    if a == sorted(a):
        break

print("試行回数" + str(counter) + "回")
