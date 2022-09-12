from itertools import count, cycle

try:
    x = int(input('Введите целое число, с которого начнет работу итератор: '))
    y = int(input('Введите целое число, на котором итератор закончит свою работу: '))
    stroka = input('Введите элементы списка для итератора: ')
    print(f'Целые числа, начиная с {x} и заканчивая {y}')
    for el in count(x):
        if el > y:
            break
        else:
            print(el)
    print(f'Итератор, повторяющий введенный ранее список ({stroka}) до достижения {y} итерации: ')
    с = 0
    for elnt in cycle(stroka):
        if с > y - 1:
            break
        print(elnt)
        с += 1

except ValueError:
    print('Требуется ввести число, а не строку символов')