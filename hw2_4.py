stroka = (input("Введите строку из нескольких слов, разделённых пробелами: ")).split()
print(stroka)

for i, el in enumerate(stroka):
    if len(el) <= 10:
        print(f'{i+1} элемент:, {el}')
    else:
        print(f'{i+1} элемент:, {el[:10]}')