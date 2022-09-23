class Date:
    def __init__(self, date: str):
        self.date = date

    @classmethod
    def preobrazovatel_date(cls, date_str: str):
        day, month, year = map(int, date_str.split('-'))
        return day, month, year

    @staticmethod
    def validate_date(date_str: str):
        day, month, year = map(int, date_str.split('-'))
        if (day <= 31 and month <= 12 and year <= 2999) == True:
            return 'все числа введены корректно'
        else:
            return 'числа дат Некорректны'


try:
    my_date = Date(input('Введите дату в формате «день-месяц-год»: '))
    print(Date.preobrazovatel_date(my_date.date))
    print(Date.validate_date(my_date.date))
except ValueError:
    print('Требуется ввести дату в формате «день-месяц-год»')