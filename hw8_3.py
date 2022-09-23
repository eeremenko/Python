class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

    def __str__(self):
        return self.txt


def is_digit(string):  # проверка на целые и десятичные числа
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


my_list = []
while True:
    try:
        value = input('Введите очередное число в список (нажмите s - для выхода): ')
        if value == 's':  # если введен 's', то цикл завершается и выводится получившийся список
            print(f'Result: {my_list}')
            break
        if not is_digit(value):  # если введено не число, то вызывается исключение
            raise OwnError('Введенное значение должно быть числом')
        my_list.append(float(value)) if '.' in value else my_list.append(int(value))
    except OwnError as err:
        print(err)