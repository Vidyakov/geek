# Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать,
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
# ● написать общий вывод: какой из трёх вариантов лучше и почему.

import timeit
import cProfile as test

# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

first_var = """
def first_variant(MINVAL, MAXVAL, LONGARR):
    import random
    rand_arr = [random.randint(MINVAL, MAXVAL) for _ in range(LONGARR)]
    minimum = [MAXVAL, None]
    maximum = [MINVAL, None]
    counter = 0

    for i in rand_arr:
        if i > maximum[0]:
            maximum = i, counter
        if i < minimum[0]:
            minimum = i, counter
        counter += 1

    slice = rand_arr[maximum[1]+1:minimum[1]]
    if len(slice) == 0:
        slice = rand_arr[minimum[1]+1:maximum[1]]

    sum = 0
    for i in slice:
        sum += i
    return sum

# first_variant(-100, 100, 400)
"""
# number = 1000
# Длина массива = 50, время выполнения = 0.05753
# Длина массива = 100, время выполнения = 0.1068924
# Длина массива = 200, время выполнения = 0.2154569
# Длина массива = 400, время выполнения = 0.414461
# test.run('first_variant(-100, 100, 400)')

second_var = """
def second_variant(MINVAL, MAXVAL, LONGARR):
    import random
    rand_arr = [random.randint(MINVAL, MAXVAL) for _ in range(LONGARR)]
    min_val = rand_arr.index(min(rand_arr))
    max_val = rand_arr.index(max(rand_arr))
    if min_val < max_val:
        return sum(rand_arr[min_val + 1:max_val])
    else:
        return sum(rand_arr[max_val + 1:min_val])
    
# second_variant(-100, 100, 400)
"""
# number = 1000
# Длина массива = 50, время выполнения = 0.06060120000000001
# Длина массива = 100, время выполнения = 0.102673
# Длина массива = 200, время выполнения = 0.2081151
# Длина массива = 400, время выполнения = 0.3998744
# test.run('second_variant(-100, 100, 400)')


# Третий вариант не написал.
# Графики функций линейны. Вторая функция работает чуть. Кардинальной разницы не заметил.
