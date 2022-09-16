class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.height = 5

    def asphalt_mass(self):
        asphalt_mass = self._length * self._width * self.weight * self.height / 1000
        print(f'Для покрытия всего дорожного полотна неободимо {round(asphalt_mass)} тонн асфальта')


try:
    my_length = int(input('Введите длинну дорожного полотна, м: '))
    my_width = int(input('Введите ширину дорожного полотна, м: '))
    r = Road(my_length, my_width)
    r.asphalt_mass()
except ValueError:
    print('Требуется ввести число, а не строку символов')