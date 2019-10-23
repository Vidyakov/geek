# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
from collections import Counter


counter = Counter()
number_of_product = int(input('Введите количество производств: '))

for i in range(number_of_product):
    name = input('Введите название производство: ')
    for v in range(4):
        profit = float(input(f'Введите профит {name} за {v+1} квартал: '))
        counter[name] += profit

all_profit = sum(counter.values())/number_of_product

print('*** ' * 15)
print(f'Средняя прибыль предприятий: {all_profit}')

for i in counter:
    if counter[i] > all_profit:
        print(f'Показатели производства {i} выше среднего')
    else:
        print(f'Показатели {i} ниже среднего')