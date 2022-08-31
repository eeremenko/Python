time = int(input('Введите время в секундах: '))
min = time // 60
hour = time // 3600
sec = time
print(f'Result: {hour}:{min}:{sec}')