filename = input('Введите имя файла с расширением: ')
out_f = open(filename, 'w',encoding='utf-8')
print('Введите построчно информацию, которая будет записана в файл. Пустой Enter - завершение работы:''\n')
while True:
    stroka = input()
    if stroka == '':
        break
    out_f.write(stroka + '\n')
out_f.close()