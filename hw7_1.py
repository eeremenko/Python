class Matrix:
    def __init__(self, mx_list):
        self.mx_list = mx_list

    def __str__(self):
        for stroka in self.mx_list:
            for elem in stroka:
                print(f"{elem:10}", end="")
            print()
        return ''

    def __add__(self, other):
        for elem_1 in range(len(self.mx_list)):
            for elem_2 in range(len(other.mx_list[elem_1])):
                self.mx_list[elem_1][elem_2] = self.mx_list[elem_1][elem_2] + other.mx_list[elem_1][elem_2]
        return Matrix.__str__(self)


print("Первая матрица получилась:")
m = Matrix([[-10, 10, 20], [-1, 10, 5], [5, 10, -20], [10, 10, 0]])
print(m.__str__())
print("Вторая матрица получилась:")
new_m = Matrix([[-20, 10, 0], [10, 0, 20], [0, 20, -10], [20, 20, -70]])
print(m.__str__())
print("Сумма матриц:")
print(m.__add__(new_m))