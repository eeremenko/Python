def int_func(stroka):
    result = []
    for i in range(len(stroka)):
        result.append(stroka[i][0:1].title() + stroka[i][1:])

    return ' '.join(result)

list = input('Введите строку из слов, разделенных пробелом: ').split()
print(int_func(list))