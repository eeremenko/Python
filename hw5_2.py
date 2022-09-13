my_f = open('111.txt')
stroka = 0
total_word = 0
for i in my_f:
    stroka += 1
    marker = 0
    word = 0
    for j in i:
        if j != ' ' and marker == 0:
            word += 1
            marker = 1
        elif j == ' ':
            marker = 0

    print('В строке ', stroka, ' содержится ', word, 'слов')
    total_word += word

print('В файле ', my_f.name, 'содержится ', stroka, 'строк и', total_word, ' слов')
my_f.close()