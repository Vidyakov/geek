x1 = float(input('Введите X1: '))
y1 = float(input('Введите Y1: '))
x2 = float(input('Введите X2: '))
y2 = float(input('Введите Y2: '))

b = x1*y2 - x2*y1
k = y1 - y2
myy = x2 -x1

if b == 0:
    print(f'Уравнение прямой: {myy}y={-k}x')
elif b > 0:
    print(f'Уравнение прямой: {myy}y={-k}x{-b}')
elif b < 0:
    print(f'Уравнение прямой: {myy}y={-k}x+{b}')