class Kletka:
    def __init__(self, count_cell):
        self.count_cell = int(count_cell)

    def __add__(self, other):
        return f'В результате объединения двух клеток - размер общей клетки равен: {self.count_cell + other.count_cell} ячеек'

    def __sub__(self, other):
        rezult = self.count_cell - other.count_cell
        return f'В результате вычитания двух клеток - размер конечной клетки равен: {rezult} ячеек' if rezult > 0 else 'Операцию вычитания с данными клетками выполнять нельзя, т.к. у второй клетки ячеек больше'

    def __mul__(self, other):
        return f'В результате умножения двух клеток - создалась общая клетка, количество ячеек в которой равно: {self.count_cell * other.count_cell}'

    def __truediv__(self, other):
        return f'В результате деления двух клеток - размер конечной клетки равен: {self.count_cell // other.count_cell} ячеек'

    def make_order(self, row):
        result = ''
        for i in range(int(self.count_cell / row)):
            result += '*' * row + '\n'
        result += '*' * (self.count_cell % row) + '\n'
        return result


c_1 = int(input('Введите количество ячеек в Первой клетке: '))
c_2 = int(input('Введите количество ячеек во Второй клетке: '))
n = int(input('Введите количество ячеек в ряду для организации каждой Клетки: '))
cell_1 = Kletka(c_1)
cell_2 = Kletka(c_2)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)

print(f'Результат организации ячеек Первой клетки по рядам по {n} ячеек в каждом ряду:\n{cell_1.make_order(n)}')
print(f'Результат организации ячеек Второй клетки по рядам по {n} ячеек в каждом ряду:\n{cell_2.make_order(n)}')
