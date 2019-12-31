# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.
import random

MINVAL = -100
MAXVAL = 100
LONGARR = 20

rand_arr = [random.randint(MINVAL, MAXVAL) for _ in range(LONGARR)]
print(f'Массив случайных чисел:\n{rand_arr}')

max_negative = MINVAL
for i in rand_arr:
    if max_negative < i < 0:
        max_negative = i


print(f'{"*** " * 10}\nНаибольшее отрицательное значение: {max_negative}')