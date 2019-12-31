# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

# Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления, задача решается в несколько строк.
# Для прокачки алгоритмического мышления такой вариант не подходит.
# Поэтому использование встроенных функций для перевода из одной системы счисления в другую в данной задаче под запретом.
# Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.
from collections import deque

first = input('Первое шестнадцатиричное число (в верхнем регистре): ')
second = input('Второе шестнадцатиричное число (в верзнем регистре): ')

# Делаю массивы
add1 = deque(first)
add2 = deque(second)
multi1 = deque(first)
multi2 = deque(second)

# Словарь возможных шестнадцатиричных значений и обратынй ему
my = {}
some = {}

# Генерирую словари
score = 0
for i in '0123456789ABCDEF':
    my[i] = score
    score += 1

score = 0
for i in '0123456789ABCDEF' * 16 :
    some[score] = i
    score += 1

result_addition = deque()
def addition(n):
    a = add1.pop() if len(add1) > 0 else '0'
    b = add2.pop() if len(add2) > 0 else '0'
    sum_ = my[a] + my[b] + n
    result_addition.appendleft(some[sum_])
    n = sum_ // 16
    if n or len(add1) + len(add2) != 0:
        addition(n)

addition(0)
print(f'Сумма: {list(result_addition)}')


# Работает неверно!
result_multiplication = deque()
def multiplication(n):
    a = multi1.pop() if len(multi1) > 0 else '0'
    b = multi2.pop() if len(multi2) > 0 else '0'
    multi = my[a] * my[b] + n # Этот момент нужно подправить . Т.к. берется "0" и из-за него теряется разряд
    result_multiplication.appendleft(some[multi])
    n = multi // 16
    if n or len(multi1) + len(multi2) != 0:
        multiplication(n)

multiplication(0)
print(f'Произведение: {list(result_multiplication)}')