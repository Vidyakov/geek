# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.
import random

MINRANDVAL = 0
MAXRANDVAL = 100
ARRLONG = 50
score = 0

rand_array = [random.randint(MINRANDVAL, MAXRANDVAL) for _ in range(ARRLONG)]
even_key = []
print(f'Массив случайных чисел\n{rand_array}')

for i in rand_array:
    if i % 2 == 0:
        even_key.append(score)
    score += 1

print(f'{"*** " * 25}\nИндексы четных чисел\n{even_key}')