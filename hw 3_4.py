def  my_func(x, y):
    return 1 / x ** abs(y)

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

print(my_func(a, -b))
