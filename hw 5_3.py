with open('111.txt', 'r', encoding='utf-8') as f:
    workers = {}
    sredn_zp = 0
    num = 0
    print('У следующих сотрудников зарплата меньше 20 тыс.руб.:')
    for line in f:
        num += 1
        key, value = line.split()
        sredn_zp += float(value)
        if float(value) < 20000:
            print(f'{key}')
    print('Средняя величина дохода сотрудников составляет: %.2f' % (sredn_zp / num))