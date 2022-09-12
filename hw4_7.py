def fact(x):
    a = 1
    for i in range(1, x + 1):
        a = a * i
        yield a


try:
    n = int(input("Введите число, чей факториал требуется посчитать: "))
    for el in fact(n):
        print(el)
except ValueError:
    print('Требуется ввести число, а не строку символов')