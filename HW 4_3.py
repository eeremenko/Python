a = 20
b = 240
spisok = [el for el in range(a, b + 1) if (el % 20 == 0) or (el % 21 == 0)]
print(spisok)