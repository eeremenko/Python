def my_summ():
    res = 0
    while True:
        numbers = input('Введите строку чисел, разделенных пробелом. GACHI если хотите завершить программу: ').split()
        for i in numbers:
            if i == 'GACHI':
                print(f'Итоговая сумма: {res}')
                return
            else:
                res += int(i)
                print(f'На данном этапе сумма равна: {res}')

my_summ()