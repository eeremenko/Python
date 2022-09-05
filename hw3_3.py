def my_func(x, y, z):
    mass = [x,y,z]
    mass.remove(min(x,y,z))
    return sum(mass)

a = int(input('Введите число а:'))
b = int(input('Введите число b:'))
c = int(input('Введите число c:'))

print(my_func(a, b ,c))