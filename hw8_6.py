from abc import ABC, abstractmethod


class Department(ABC):  # абстрактный класс подразделение компании, которое принимает технику
    @abstractmethod
    def add(self, type_technic, data):
        pass


class OwnError(Exception):  # собственный класс исключение типа объекта
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class Storage:  # класс склада техники
    def __init__(self):
        self.__storage = {}

    @property
    def storage(self):  # получение закрытого атрибута с типом словарь
        return self.__storage

    def add_technic(self, technic,
                    number):  # добавление техники на склад, включает валидацию с типом оргтехники и количеством
        try:
            if not isinstance(number, int):
                raise OwnError('Количество оргтехники должно быть целым числом')
            technic.params['Количество'] = number
            if not self.__storage.get(technic.type_technic):
                self.__storage[technic.type_technic] = {technic.name: technic.params}
            else:
                self.__storage[technic.type_technic].setdefault(technic.name, technic.params)
        except OwnError as err:
            print(err)

    def transfer_to_department(self, technic,
                               department):  # передача техники подразделению: какую оргтехнику какому департаменту
        department.add(technic.type_technic, self.__storage.get(technic.type_technic))


class TransportDepartment(
    Department):  # транспортное подразделение, реализация абстрактного класса Подразделение компании
    def __init__(self):
        self.__storage = {}

    @property
    def storage(self):
        return self.__storage

    def add(self, type_technic, data):  # добавляет технику в подразделение: тип оргтехники и дата передачи
        if not self.__storage.get(type_technic):
            self.__storage[type_technic] = data
        else:
            self.__storage[type_technic].setdefault(data)


class OfficeTechnics:  # базовый класс офисной техники
    def __init__(self, name: str, color: str):  # общие атрибуты классов наследников с указанием марки и цвета корпуса
        self.name = name
        self.color = color


class Printer(OfficeTechnics):
    def __init__(self, name: str, color: str, speed: int):
        super().__init__(name, color)
        self.type_technic = self.__class__.__name__
        self.print_speed = speed
        self.params = {'Марка': self.name, 'Цвет корпуса': self.color, 'Скорость печати': self.print_speed}


class Scanner(OfficeTechnics):
    def __init__(self, name: str, color: str, speed: int):
        super().__init__(name, color)
        self.type_technic = self.__class__.__name__
        self.scan_speed = speed
        self.params = {'Марка': self.name, 'Цвет корпуса': self.color, 'Скорость сканирования': self.scan_speed}


class Copierr(OfficeTechnics):
    def __init__(self, name: str, color: str, speed: int):
        super().__init__(name, color)
        self.type_technic = self.__class__.__name__
        self.copy_speed = speed
        self.params = {'Марка': self.name, 'Цвет корпуса': self.color, 'Скорость копирования': self.copy_speed}


class ccc(OfficeTechnics):
    pass

    printer = Printer('HP', 'Black', 12)
    scaner = Scanner('Canon', 'White', 15)
    copyr = Copierr('Canon', 'Gray', 23)
    print(f'Принтер: {printer}')
    print(f'Сканер: {scaner}')
    print(f'Копир: {copyr}')
    storage = Storage()
    storage.add_technic(printer, 20)
    storage.add_technic(scaner, 50)
    print(f'На складе: {storage.storage}')
    transportDep = TransportDepartment()
    storage.transfer_to_department(scaner, transportDep)
    print(f'Передача на хранение в подразделение transportDep: {transportDep.storage}')