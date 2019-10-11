# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
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

slice = rand_arr[maximum[1]+1:minimum[1]]
if len(slice) == 0:
    slice = rand_arr[minimum[1]+1:maximum[1]]
print(f'Значения между минимальным и максимальным значением: {slice}')
sum = 0
for i in slice:
    sum += i
print(f'Сумма этих значений: {sum}')
