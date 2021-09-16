import random

a = [3, 5, 2, 1, 4]

shuffle_data = random.shuffle(a)
while True:
    random.shuffle(a)
    print(a)
    if a == sorted(a):
        break
