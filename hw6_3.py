class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return 'Имя и фамилия сотрудника: ' + self.name + ' ' + self.surname + '\n'

    def get_total_income(self):
        return 'Доход с учетом премии: ' + str(self._income["wage"] + self._income["bonus"]) + ' р.'


try:
    new_name = input('Введите имя сотрудника: ')
    new_surname = input('Введите фамилию сотрудника: ')
    new_position = input('Введите должность сотрудника: ')
    new_wage = int(input('Введите оклад сотрудника, р.: '))
    new_bonus = int(input('Введите премию сотрудника, р.: '))

    p = Position(new_name, new_surname, new_position, new_wage, new_bonus)
    print(p.get_full_name(), p.get_total_income())
except ValueError:
    print('Требуется ввести число, а не строку символов')