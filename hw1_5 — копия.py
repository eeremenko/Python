profit = float(input("Please enter your profit: "))
loss = float(input("Please enter your loss: "))
if profit > loss:
    print('танцуй как бабочка, мы в плюсе')
    print(f'Рентаельность твоей компании составит {(profit - loss) / profit}')
    с = int(input('колличество сотрудников '))
    print(f'прибыль одного сотрудника {profit / с}')
elif profit == loss:
    print('Ты реботаешь в 0')
else:
    print('Закрывай компанию. Переписывай ее на космонавта.Беги')





