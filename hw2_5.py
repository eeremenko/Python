my_list = [7, 5, 3, 3, 2]
new_raiting = int(input("Введите новый элемент рейтинга как целое цисло: "))
i = 0
for raiting in my_list:
    if new_raiting > raiting:
        break
    i += 1
my_list.insert(i, new_raiting)
print(my_list)