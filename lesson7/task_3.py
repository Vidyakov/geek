# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда,
# делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой — не больше медианы.

import random

m = int(input('Введите натуральное число: '))

MINVAL = 0
MAXVAL = 100
LONG = 2*m + 1

rand_arr = [random.randint(MINVAL, MAXVAL) for _ in range(LONG)]
print(f' Массив случайных чисел от {MINVAL} до {MAXVAL} '.center(len(rand_arr)*4, "*"))
print(rand_arr)


new_arr = []
while len(new_arr) < LONG/2:
    val = min(rand_arr)
    rand_arr.remove(val)
    new_arr.append(val)


print(f'Медиана: {new_arr.pop()}')
