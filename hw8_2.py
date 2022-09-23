class ZeroDivisionException(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    a, b = map(int, input('Введите a и b, чтобы разделить их друг на друга: ').split())
    if b == 0:
        raise ZeroDivisionException('Деление на ноль запрещено')
    print(f'Результат деления a/b : {a / b}')
except ZeroDivisionException as err:
    print(err)
except ValueError:
    print("Вы ввели не число")