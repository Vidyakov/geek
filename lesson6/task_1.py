# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных
# программах в рамках первых трех уроков. Проанализировать результат
# и определить программы с наиболее эффективным использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
# ● проанализировать 3 варианта и выбрать оптимальный;
# ● результаты анализа (количество занятой памяти в вашей среде разработки)
#   вставить в виде комментариев в файл с кодом.
#   Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
# ● написать общий вывод: какой из трёх вариантов лучше и почему.
# Надеемся, что вы не испортили программы,
# добавив в них множество sys.getsizeof после каждой переменной, а проявили творчество,
# фантазию и создали универсальный код для замера памяти.

import random
import sys

# MacOS, 86x, Python 3.7
# Задача:
# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.


""""Этот код для всех вариантов решений"""
MINVAL = 0
MAXVAL = 100
LONGARR = 20

rand_arr = [random.randint(MINVAL, MAXVAL) for _ in range(LONGARR)]
print(f'Массив случайных чисел:\n{rand_arr}')



# Вариант №1
# memory_size = sys.getsizeof(MINVAL) + sys.getsizeof(MAXVAL) + sys.getsizeof(LONGARR) + sys.getsizeof(rand_arr)
#
# minimum = [MAXVAL, None]
# maximum = [MINVAL, None]
# counter = 0
#
# for i in rand_arr:
#     if i > maximum[0]:
#         maximum = i, counter
#         memory_size += sys.getsizeof(maximum)
#     if i < minimum[0]:
#         minimum = i, counter
#         memory_size += sys.getsizeof(minimum)
#     counter += 1
#     memory_size += sys.getsizeof(i) + sys.getsizeof(counter)
#
# slice = rand_arr[maximum[1]+1:minimum[1]]
# if len(slice) == 0:
#     slice = rand_arr[minimum[1]+1:maximum[1]]
#
# memory_size += sys.getsizeof(slice)
#
# sum_ = 0
# for i in slice:
#     sum_ += i
#     memory_size += sys.getsizeof(i)
#
# memory_size += sys.getsizeof(sum_)
#
# print(f'Сумма значений: {sum_}')

# >>> print(memory_size)
# 2304


# Вариант №2

# memory_size = sys.getsizeof(MINVAL) + sys.getsizeof(MAXVAL) + sys.getsizeof(LONGARR) + sys.getsizeof(rand_arr)
#
# minimum = rand_arr.index(min(rand_arr))
# maximum = rand_arr.index(max(rand_arr))
#
# memory_size += sys.getsizeof(minimum) + sys.getsizeof(maximum)
#
# if maximum > minimum:
#     slice = rand_arr[minimum+1:maximum]
#     sum_ = sum(slice)
# else:
#     slice = rand_arr[maximum+1:minimum]
#     sum_ = sum(slice)
#
# memory_size += sys.getsizeof(slice)
# memory_size += sys.getsizeof(sum_)
#
# print(f'Сумма значний: {sum_}')


# >>> print(memory_size)
# 516


# Вариант №3

# memory_size = sys.getsizeof(MINVAL) + sys.getsizeof(MAXVAL) + sys.getsizeof(LONGARR) + sys.getsizeof(rand_arr)
#
# minimum = rand_arr.index(min(rand_arr))
# maximum = rand_arr.index(max(rand_arr))
#
# memory_size += sys.getsizeof(minimum) + sys.getsizeof(maximum)
#
# counter = 0
# sum_ = 0
#
# for i in rand_arr:
#     if minimum < counter < maximum if minimum < maximum else maximum < counter < minimum:
#         sum_ += i
#     counter += 1
#     memory_size += sys.getsizeof(i) + sys.getsizeof(counter)
#
#
# print(f'Сумма значений: {sum_}')
# print(memory_size)

# >>> print(memory_size)
# 1512


# Второй вариант выигрывает с большим отрывом. Видимо это из-за того, что в нем не используются циклы
# и используются только функции из стандартной библиотеки, которые более экономные. Когда
# писал третий вариант, думал он будет самым оптимальным т.к. сделал его без срезов.
# Это оказалось не лучшей идеей)
