# Определить, какое число в массиве встречается чаще всего.
import random

MINVAL = 0
MAXVAL = 100
LONGARR = 20

rand_arr = [random.randint(MINVAL, MAXVAL) for _ in range(LONGARR)]
print(f'Массив случайных чисел:\n{rand_arr}')

total = 0
value = MINVAL
for i in rand_arr:
    score = 0
    for v in rand_arr:
        if i == v:
            score += 1
    if score > total:
        total = score
        value = i

print(f'{"*** " * 10}\nЧисло {value} встретилось {total} раза')
