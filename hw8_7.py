class OwnError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class ComplexNum:  # класс «Комплексное число»
    def __init__(self, a=0, b=0):
        self._num = complex(a, b)

    @property
    def num(self):
        return self._num

    def __add__(self, other):  # перегружаем метод сложения для комплексных чисел
        try:  # валидация аргументов
            if isinstance(other, ComplexNum):
                return ComplexNum(self.num + other.num)
            elif isinstance(other, complex):
                return ComplexNum(self.num + other)
            raise OwnError('Введенное число должно быть комплексным')
        except OwnError as err:
            print(err)

    def __mul__(self, other):  # перегружаем метод умножения комплексных чисел
        try:
            if isinstance(other, ComplexNum):
                return ComplexNum(self.num * other.num)
            elif isinstance(other, complex):
                return ComplexNum(self.num * other)
            raise OwnError('Введенное число должно быть комплексным')
        except OwnError as err:
            print(err)

    def __str__(self):
        return f'результат: {self._num}'


x = ComplexNum(1, 2)
y = ComplexNum(3, 4)
print(x + y)
print(x + complex(5, 6))
print(x * y)
print(x + 1)