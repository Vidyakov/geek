a = int(input("Введите 1 число: "))
b = int(input("Введите 2 число: "))
c = int(input("Введите 3 число: "))

if a > b:
    if a > c:
        if b > c:
            print(b)
        elif c > b:
            print(c)
if b > a:
    if b > c:
        if a > c:
            print(a)
        elif c > a:
            print(c)
if c > a:
    if c > b:
        if b > a:
            print(b)
        elif b < a:
            print(a)