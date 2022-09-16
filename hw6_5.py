
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return f'Сейчас запущена отрисовка {self.title}'


class Pencil(Stationery):
    def draw(self):
        return f'Сейчас запущена отрисовка {self.title}'


class Handle(Stationery):
    def draw(self):
        return f'Сейчас запущена отрисовка {self.title}'


my_pen = Pen('ручкой')
print(my_pen.draw())
my_pencil = Pencil('карандашем')
print(my_pencil.draw())
my_handle = Handle('маркером')
print(my_handle.draw())