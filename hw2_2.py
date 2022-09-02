list = []
while True:
    elem = input("Введите элемент списка: ")
    list.append(elem)
    elem_end = (input("Это все элементы списка? (Y/N)")).upper()
    if elem_end == "Y":
        break
print(list)
print(len(list))

i = 0

while i < len(list) - 1:
    if i % 2 == 0:
        list[i], list[i + 1] = list[i + 1], list[i]
    i += 1

print(list)