new_list = [el for el in range(1, 20)]
sum = 0
with open("home5.txt", "a",encoding='utf-8') as file:
    for element in new_list:
        sum += element
        file.write(str(element))
        file.write(' ')

print('Сумма числе в файле равна:', sum)