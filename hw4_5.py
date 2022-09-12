from functools import reduce


def my_func(prev_el, el):
    return prev_el * el


a = 1
b = 10
spisok = [el for el in range(a, b + 1) if el % 2 == 0]
print(spisok)
print('результат вычисления произведения всех элементов списка: ', reduce(my_func, spisok))