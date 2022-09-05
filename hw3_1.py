def my_del (x,y):
    try:
        return x / y
    except ZeroDivisionError:
        return('Деление на 0 запрещено')
2
a =  int(input('Введите число А: '))
b = int(input('Введите число B: '))
print(my_del(a, b))