# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы
import random

MINVAL = 0
MAXVAL = 100
LONGARR = 10

minimum = [MAXVAL, None]
maximum = [MINVAL, None]
counter = 0

rand_arr = [random.randint(MINVAL, MAXVAL) for _ in range(LONGARR)]
print(f'Массив случайных чисел\n{rand_arr}')

for i in rand_arr:
    if i > maximum[0]:
        maximum = i, counter
    if i < minimum[0]:
        minimum = i, counter
    counter += 1
print(f'Минимальное значение и его позиция: {minimum}\nМаксимальное значение и его позиция: {maximum}')

rand_arr[minimum[1]] = maximum[0]
rand_arr[maximum[1]] = minimum[0]
print(f'{"*** " * 10}\nПосле смены\n{rand_arr}')
