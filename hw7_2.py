from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @property
    def rashod(self):
        pass

    @abstractmethod
    def abstract(self):
        pass


class Palto(Clothes):
    @property
    def rashod(self):
        return f'{self.param / 6.5 + 0.5 :.2f}'
    #        return f'Для пошива пальто нужно: {self.param / 6.5 + 0.5 :.2f} ткани'

    def abstract(self):
        return 'Возвращает решение абстрактной функции для Пальто'


class Kostum(Clothes):
    @property
    def rashod(self):
        return f'{2 * self.param + 0.3 :.2f}'
    #        return f'Для пошива костюма нужно: {2 * self.param + 0.3 :.2f} ткани'

    def abstract(self):
        return 'Возвращает решение абстрактной функции для Костюма'


my_palto = Palto(400)
my_kostum = Kostum(55)

print(f'Для пошива пальто нужно: {my_palto.rashod} ткани')
print(f'Для пошива костюма нужно: {my_kostum.rashod} ткани')
print(f'Общий расход ткани для пошива пальто и костюма нужно: {str(float(my_palto.rashod) + float(my_kostum.rashod))} ткани')
print(my_palto.abstract())
print(my_kostum.abstract())