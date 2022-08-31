n = int(input("Please enter number (n): "))
max_num = 0
while n > 0:
    n1 = n % 10
    if n1 == 9:
        max_num = n1
        break
    elif n1 > max_num:
        max_num = n1
    n = n // 10
print('Максимальное число в вашем номере: ', max_num)
