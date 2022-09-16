class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Автомобиль {self.name} поехал.'

    def stop(self):
        return f'\nАвтомобиль {self.name} остановился.'

    def turn(self, direction):
        return f'\nАвтомобиль {self.name} повернул {direction}'

    def show_speed(self):
        return f'\nТекущая скорость автомобиля равна: {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nВаша скорость превышает допустимую! Скрость равна: {self.speed}'
        else:
            return f'\nСейчас ваша скорость равна: {self.speed}. И она допустима.'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nВаша скорость превышает допустимую! Скрость равна: {self.speed}'
        else:
            return f'\nСейчас ваша скорость равна: {self.speed}. И она допустима.'


class PoliceCar(Car):
    pass


town = TownCar(70, 'blue', 'Киа', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('left'), town.stop())

sport = SportCar(170, 'red', 'Феррари', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('left'), sport.stop())

work = WorkCar(30, 'red', 'Камаз', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('right'), work.stop())

police = PoliceCar(100, 'yellow', 'Форд', True)
print('4:\n' + police.go(), police.show_speed(), police.turn('right'), police.stop())