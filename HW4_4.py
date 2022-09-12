spisok = list(map(int, input('Введите элементы списка в виде целых чисел через пробел ').split()))
print(spisok)
new_spisok = [el for el in spisok if spisok.count(el) == 1]
print(new_spisok)