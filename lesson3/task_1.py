# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

MAXVAL = 100
MINVAL = 2

bigrange = [i for i in range(MINVAL, MAXVAL)]
smallrange = [i for i in range(2, 10)]
total = 0

for i in bigrange:
    score = 0
    for v in smallrange:
        if i % v != 0:
            break
        else:
            score += 1
        if score == 9:
            total += 1

print(total)
