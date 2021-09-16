import random

a = [3, 5, 2, 1, 4]

shuffle_data = random.shuffle(a)
while True:
    if a == sorted(a):
        print(a)
        break
    random.shuffle(a)
    print(a)