try:
    spisok = list(map(int, input('Введите элементы списка в виде целых чисел через пробел ').split()))
    print(spisok)
    new_spisok = [spisok[i] for i in range(1, len(spisok)) if spisok[i - 1] < spisok[i]]
    print(new_spisok)
except ValueError:
    print('Требуется ввести целое число, а не строку символов или десятичное число')